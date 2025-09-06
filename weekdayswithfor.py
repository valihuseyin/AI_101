# Pseudo-code:
# 1. Create a list of days of the week.
# 2. For each day in the list:
#    a. If the day is Saturday or Sunday:
#        - Print the day and "A chance to sleep in!"
#    b. Else if the day is Friday:
#        - Print the day and "Off to work."
#        - Print "Ready for the weekend!"
#    c. Else:
#        - Print the day and "Off to work."

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days_of_week:
    if day == "Saturday" or day == "Sunday":
        print(f"{day}: A chance to sleep in!")
    elif day == "Friday":
        print(f"{day}: Off to work.")
        print("Ready for the weekend!")
    else:
        print(f"{day}: Off to work.")
    
    # Pseudo-code:
    # 1. Loop over numbers from 1 to 30.
    # 2. For each number:
    #    a. If the number is divisible by both 3 and 5:
    #        - Print "FizzBuzz"
    #    b. Else if the number is divisible by 3:
    #        - Print "Fizz"
    #    c. Else if the number is divisible by 5:
    #        - Print "Buzz"
    #    d. Else:
    #        - Print the number

    for num in range(1, 31):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

            # Use a set when you need to store unique items and only care about their existence, not any associated values.
            # Use a dictionary when you need to associate values with keys, allowing you to store key-value pairs for fast lookup.