# Define a function for bitwise XOR
def bitwise_xor(a, b):
    return a ^ b

# Prompt the user for input
try:
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    
    # Calculate the bitwise XOR
    result = bitwise_xor(num1, num2)
    
    # Print the result
    print(f"Result of bitwise XOR: {result}")
except ValueError:
    print("Please enter valid integers.")
