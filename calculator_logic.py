def calculate():
    print("--- 🧮 Robust Logic Calculator ---")
    
    try:
        # Taking inputs
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        # Logic for operations
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            # The code will jump to 'except' if num2 is 0
            result = num1 / num2
        else:
            print("❌ Error: Invalid Operator!")
            return

        print(f"✅ Result: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("❌ Error: Please enter valid numeric values.")
    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero! Stay logical.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculate()
