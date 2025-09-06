# Pseudo-code:
# 1. Ask the user to input a number.
# 2. Convert the input to an integer.
# 3. Initialize an empty list to store divisors.
# 4. Loop through numbers from 1 to the input number (inclusive).
# 5. For each number, check if it divides the input number evenly (remainder is 0).
# 6. If yes, add it to the list of divisors.
# 7. Print the list of divisors.
def find_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

def print_divisors(divisors):
    print("Divisors are:", divisors)

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    divisors = find_divisors(number)
    print_divisors(divisors)
