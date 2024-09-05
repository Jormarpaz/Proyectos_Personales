import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    user_id = session["user_id"]

    rows = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    cash = rows[0]["cash"]

    stocks = db.execute("""
        SELECT symbol, SUM(shares) AS total_shares
        FROM transactions
        WHERE user_id = ?
        GROUP BY symbol
        HAVING total_shares > 0
    """, user_id)

    portfolio = []
    total_value = cash

    for stock in stocks:
        symbol = stock["symbol"]
        shares = stock["total_shares"]
        stock_info = lookup(symbol)
        if stock_info:
            current_price = stock_info["price"]
            total_stock_value = shares * current_price
            portfolio.append({
                "symbol": symbol,
                "shares": shares,
                "current_price": usd(current_price),
                "total_value": usd(total_stock_value)
            })
            total_value += total_stock_value

    return render_template("index.html", cash=usd(cash), portfolio=portfolio, total_value=usd(total_value))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("must provide stock symbol")

        try:
            shares = int(shares)
            if shares <= 0:
                return apology("shares must be a positive integer > 0")
        except ValueError:
            return apology("shares must be a positive integer > 0")

        stock = lookup(symbol)

        if stock is None:
            return apology("invalid stock symbol")

        price = stock["price"]

        user_id = session["user_id"]
        rows = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        cash = rows[0]["cash"]

        total_cost = price * shares

        if cash < total_cost:
            return apology("cant afford")

        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                   user_id, symbol, shares, price)
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_cost, user_id)

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    user_id = session["user_id"]

    transactions = db.execute("""
        SELECT symbol, shares, price, transacted
        FROM transactions
        WHERE user_id = ?
        ORDER BY transacted DESC
    """, user_id)

    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 403)

        elif not request.form.get("password"):
            return apology("must provide password", 403)

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    session.clear()

    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("must provide stockk symbol")

        stock = lookup(symbol)

        if stock is None:
            return apology("invalid stock symbol")

        return render_template("quoted.html", symbol=stock["symbol"], price=usd(stock["price"]))

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("must provide username")

        elif db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username")):
            return apology("username already exists")

        elif not password:
            return apology("must provide password")

        elif not confirmation:
            return apology("must provide confirmation password")

        elif password != confirmation:
            return apology("passwords do not match")

        try:
            password_hash = generate_password_hash(password)
            db.execute("INSERT INTO users(username,hash) VALUES (?,?)", username, password_hash)
        except ValueError:
            return apology("there was an error when inserting into de database")

        return redirect("/login")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    user_id = session["user_id"]

    if request.method == "GET":
        stocks = db.execute("""
            SELECT symbol, SUM(shares) AS total_shares
            FROM transactions
            WHERE user_id = ?
            GROUP BY symbol
            HAVING total_shares > 0
        """, user_id)

        return render_template("sell.html", stocks=stocks)

    else:
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("must select a stock", 400)

        if not shares or int(shares) <= 0:
            return apology("must provide a positive number of shares", 400)

        shares = int(shares)

        stock = db.execute("""
            SELECT SUM(shares) AS total_shares
            FROM transactions
            WHERE user_id = ? AND symbol = ?
            GROUP BY symbol
        """, user_id, symbol)

        if len(stock) != 1 or stock[0]["total_shares"] < shares:
            return apology("not enough shares", 400)

        stock_info = lookup(symbol)
        if not stock_info:
            return apology("invalid stock symbol", 400)

        current_price = stock_info["price"]
        total_sale_value = shares * current_price

        db.execute("""
            INSERT INTO transactions (user_id, symbol, shares, price)
            VALUES (?, ?, ?, ?)
        """, user_id, symbol, -shares, current_price)

        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total_sale_value, user_id)

        return redirect("/")
