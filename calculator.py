# This program implements a simple calculator that can perform basic arithmetic operations such as addition, subtraction, multiplication, and division. It takes user input for the operation they want to perform and the two numbers involved. The program checks if the input is valid (i.e., ensuring the user enters numbers and valid operations). If the user enters an invalid operation or tries to divide by zero, the program handles the error gracefully by displaying an appropriate message.


# Declaring a dictionary to make the code dynamic and calling lambda function for calculation
operations = {
    'addition' : lambda x, y : x + y,
    'subtraction' : lambda x, y : x - y,
    'multiplication' : lambda x, y : x * y,
   'division' : lambda x, y : x / y if y!= 0 else "Cannot divide by zero"
}


# Handling Input Error
def get_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Enter only numbers.")

# taking user input
a = get_input("Enter first number (a): ")
b = get_input("Enter seecond number (b): ")

# calculating the result and storing them in variables
result_add = operations['addition'](a, b)
result_subtract = operations['subtraction'](a, b)
result_multiple = operations['multiplication'](a, b)
result_division = operations['division'](a, b)


# Displaying the result
print(f"{a} + {b} = ", result_add)
print(f"{a} - {b} = ", result_subtract)
print(f"{a} x {b} = ", result_multiple)
print(f"{a} ÷ {b} = ", result_division)