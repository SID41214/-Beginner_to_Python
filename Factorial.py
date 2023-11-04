def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

number =5  # Replace with the number for which you want to find the factorial
fact = factorial(number)
print(f"The factorial of {number} is {fact}")
