def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

try:
    # Given list
    num_list = [-1, 2, 3, 4, 5, 6, 7]

    prime_numbers = []
    non_prime_numbers = []

    for num in num_list:
        if is_prime(num) and num > 1:
            prime_numbers.append(num)
        else:
            non_prime_numbers.append(num)

    print("Prime Numbers:", prime_numbers)
    print("Non-Prime Numbers:", non_prime_numbers)

except Exception as e:
    print("An error occurred:", e)
