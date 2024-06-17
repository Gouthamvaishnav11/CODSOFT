
def add(num1, num2):
    return float(num1) + float(num2)

def subtract(num1, num2):
    return float(num1) - float(num2)

def multiply(num1, num2):
    return float(num1) * float(num2)

def divide(num1, num2):
    if float(num2) == 0:
        return "Error! Division by zero."
    else:
        return float(num1) / float(num2)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = input("Enter your first number: ")
    num2 = input("Enter your second number: ")
    action = input("Enter the operation you would like to perform (+, -, *, /): ")
    
    calculation_function = operations.get(action)
    if calculation_function:
        answer = calculation_function(num1, num2)
        print(f"{num1} {action} {num2} = {answer}")
    else:
        print("Invalid operation!")
        return

    continue_calculation = input("Would you like to continue calculation? Type y/n: ")
    if continue_calculation.lower() == "y":
        calculator()
    else:
        print("Thank you for using the calculator.")

calculator()

