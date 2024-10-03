# Function to perform the calculation based on the operator
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Handle division by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed!"
        return num1 / num2
    else:
        return "Invalid operator!"

# Function to run the calculator
def calculator():
    try:
        # Prompt the user to input two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Prompt the user to choose an operation
        operator = input("Choose an operation (+, -, *, /): ")
        
        # Perform the calculation and display the result
        result = calculate(num1, num2, operator)
        print(f"The result is: {result}")
    
    except ValueError:
        print("Error: Please enter valid numbers!")

# Run the calculator
calculator()
