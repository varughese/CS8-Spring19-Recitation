# Program make a simple calculator that can add, subtract, multiply and divide using functions

# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


# This function is the memory
def memorized(result):
    new_file = open("memory.txt", mode="w", encoding="utf-8")
    new_file.write(str(result))
    new_file.close()


# This function is the restore
def restore():
    file = open("memory.txt", mode="r", encoding="utf-8")
    return int(file.read())


# This function displays the menu
def menu():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Memory")
    print("6.Restore")
    print("0.Exit")


# Print menu
menu()
# Take input from the user
choice = input("Enter choice(1/2/3/4):")
result = 0
restored = False
while (choice != '0'):
    if choice == '1':
        if not restored:
            num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = add(num1, num2)
        print(num1, "+", num2, "=", result)
        # reset the flag
        restored = False
    elif choice == '2':
        if not restored:
            num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = subtract(num1, num2)
        print(num1, "-", num2, "=", result)
        # reset the flag
        restored = False
    elif choice == '3':
        if not restored:
            num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = multiply(num1, num2)
        print(num1, "*", num2, "=", result)
        # reset the flag
        restored = False
    elif choice == '4':
        if not restored:
            num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = divide(num1, num2)
        print(num1, "/", num2, "=", result)
        # reset the flag
        restored = False
    elif choice == '5':
        memorized(result)
        print(result, " was memorized")
        # reset the flag
        restored = False
    elif choice == '6':
        num1 = restore()
        restored = True
        print(result, " was restored as the first number")
    elif choice != '0':
        print("Invalid input")

    # Print menu
    menu()
    # Take input from the user
    choice = input("Enter choice(1/2/3/4):")
