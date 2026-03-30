def calculator():
    print("Simple Calculator")

    print("3. Multiply")
    choice = input("Enter choice: ")

    if choice == "3":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a * b)

if __name__ == "__main__":
    calculator()