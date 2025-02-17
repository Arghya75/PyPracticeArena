# This program takes an integer input from the user and checks whether the number is even or odd. If the number is divisible by 2 then it is even otherwise it is odd.


# Function to check the number is even or odd
def is_even(num):
    return num % 2 == 0


# handling input errors
while True:
    try:
        n = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid input! Please enter an integer number.")

# evaluating and printing the result
result = is_even(n)
if result:
    print(f"{n} is an even number")
else:
    print(f"{n} is an odd number")