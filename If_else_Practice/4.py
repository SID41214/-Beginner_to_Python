#divisible by 3 or not withou using modulo operator
# Get a number from the user
number = int(input("Enter a number: "))

# Initialize a variable to keep track of the number
remaining = abs(number)

# Subtract 3 from the remaining number until it's less than 3
while remaining >= 3:
    remaining -= 3

# Check if the remaining number is 0
if remaining == 0:
    print(f"{number} is divisible by 3.")
else:
    print(f"{number} is not divisible by 3.")
