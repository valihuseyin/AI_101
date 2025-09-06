# Pseudo-code:
# 1. Get the score from the user as input.
# 2. Convert the input to an integer.
# 3. Check the score range:
#    - If score is between 0 and 59, grade is F.
#    - If score is between 60 and 69, grade is D.
#    - If score is between 70 and 79, grade is C.
#    - If score is between 80 and 89, grade is B.
#    - If score is between 90 and 100, grade is A.
# 4. Print the corresponding letter grade.
score = int(input("Enter your score (0-100): "))

if 0 <= score <= 59:
    grade = 'F'
elif 60 <= score <= 69:
    grade = 'D'
elif 70 <= score <= 79:
    grade = 'C'
elif 80 <= score <= 89:
    grade = 'B'
elif 90 <= score <= 100:
    grade = 'A'
else:
    grade = 'Invalid score'

print("Your grade is:", grade)