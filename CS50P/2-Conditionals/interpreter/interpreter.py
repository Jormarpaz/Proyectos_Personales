def main():
    exp = input("Expression: ")

    x,y,z = exp.split(" ")
    x = int(x)
    z = int(z)

    if y == "+" :
        op = x + z
        print(f"{op:.1f}")
    elif y == "-" :
        op = x - z
        print(f"{op:.1f}")
    elif y == "*" :
        op = x * z
        print(f"{op:.1f}")
    elif y == "/" :
        op = x / z
        print(f"{op:.1f}")



main()
