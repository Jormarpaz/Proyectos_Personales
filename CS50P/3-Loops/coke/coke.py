def main():
    amount = 50
    coins = [25, 10, 5]
    coin = 0
    while amount > 0:
        print(f"Amount Due: {amount}")
        coin = int(input("Insert Coin: "))
        while coin not in coins:
            print(f"Amount Due: {amount}")
            coin = int(input("Insert Coin: "))

        if amount - coin <= 0:
            change = abs(amount - coin)
            print(f"Change Owed: {change}")
            break
        else:
            amount = amount - coin


main()
