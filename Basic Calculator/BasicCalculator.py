from ascii_art import logo

def add(n1, n2):
    """Add two numbers and return the result."""
    return n1 + n2

def subtract(n1, n2):
    """Subtract the numbers and return the result."""
    return n1 - n2

def multiply (n1, n2):
    """Multiply the numbers and return the result."""
    return n1 * n2

def divide (n1, n2):
    """Divide the first number with second number and return the result.

    And check the second number isn't zero.
    """
    if n2 == 0:
        print("Error: cannot divide by zero.")
        return None
    else:
        return n1 / n2

def get_valid_number(message):
    """Repeatedly check until user type a valid number."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid Number. Please try again.")

math_functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(logo)

first_num = ""
is_continue = True
while is_continue:
    if first_num == "":
        first_num = get_valid_number("What's the first number?: ")

    for function in math_functions:
        print(function)
    operator = input("Pick an operation: ")
    while operator not in math_functions:
        print("Invalid choice. Please try again.")
        operator = input("Pick an operation: ")

    second_num = get_valid_number("What's the next number?: ")

    result = math_functions[operator](first_num, second_num)
    if result is None:
        print("Operation failed.")
    else:
        print(f"{first_num} {operator} {second_num} = {result}")
        user_input = input(f"Type 'y' to continue calculating with {result},"
                           f" or type 'n' to start a new calculation: ").lower()
        if user_input != "y":
            is_continue = False
        else:
            first_num = result
