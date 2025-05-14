def calculator():
    print("Welcome to Simple Calculator!")

    while True:
        try:
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))

            print("\nChoose an operation:")
            print(" +  Addition")
            print(" -  Subtraction")
            print(" *  Multiplication")
            print(" /  Division")
            print(" q  Quit")

            choice = input("Enter the operation symbol (+, -, *, /, q): ").strip()

            if choice == '+':
                result = num1 + num2
            elif choice == '-':
                result = num1 - num2
            elif choice == '*':
                result = num1 * num2
            elif choice == '/':
                if num2 == 0:
                    print(" Error: Cannot divide by zero.")
                    continue
                result = num1 / num2
            elif choice.lower() == 'q':
                print("Exiting Calculator. Goodbye!")
                break
            else:
                print(" Invalid operation symbol.")
                continue

            print(f" Result: {num1} {choice} {num2} = {result}")

        except ValueError:
            print(" Invalid input! Please enter numeric values.")

# Run the calculator
calculator()
