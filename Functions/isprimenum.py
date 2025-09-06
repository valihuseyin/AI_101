# Pseudo-code:
# 1. Ask the user to enter a number.
# 2. Check if the number is less than 2 (not prime).
# 3. For numbers 2 and above, check divisibility from 2 up to sqrt(number).
# 4. If any divisor is found, it's not prime.
# 5. Otherwise, it's prime.

num = int(input("Enter a number: "))

if num < 2:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
        # Alternative approach using a function
        def isNumPrime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        if isNumPrime(num):
            print(f"(Function) {num} is a prime number.")
        else:
            print(f"(Function) {num} is not a prime number.")