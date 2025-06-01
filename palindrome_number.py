# This program checks whether a given number is a palindrome.
# A palindrome is a number that reads the same forwards and backwards (e.g., 121, 1331).
# The program takes user input and ensures it is a valid integer using input validation.
# It then converts the number to a string, reverses it, and compares it with the original.
# If the reversed string matches the original number, it prints "Palindrome"; otherwise, it prints "Not palindrome".
# The program also handles invalid (non-integer) input gracefully by prompting the user again until a valid number is entered.


# Defining a function to handle invalid input
def input_handling(prompt):
    while True:
        try:
            return int(input(prompt))
            break
        except ValueError:
            print("Invalid Input!")

# Taking the number to check
a = input_handling("Enter a valid integer: ")

# Converting the number into a string
b = str(a)[::-1]

# Checking Palindrome condition
if(b == a):
    print("Palindrome.")
else:
    print("Not Palindrome.")