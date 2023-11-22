import random

# Addtion

number1 = random.randint(0, 99)
number2 = random.randint(0, 99)

answer_addition = eval(input("What is " + str(number1) + "+" + str(number2) + " = "))
answer_addition_2 = number1 + number2

if answer_addition == answer_addition_2:
    print("The answer is correct")
else:
    print("The answer is wrong")

print()

# Subtraction

number3 = random.randint(0, 99)
number4 = random.randint(0, 99)

answer_subtraction = eval(input("What is " + str(number3) + "-" + str(number4) + " = "))
answer_subtraction_2 = number3 - number4
if answer_subtraction == answer_subtraction_2:
    print("The answer is correct")
else:
    print("The answer is wrong")

print()

# Multiplication
number5 = random.randint(0, 99)
number6 = random.randint(0, 99)

answer_multiplication = eval(input("What is " + str(number5) + "*" + str(number6) + " = "))
answer_multiplication_2 = number5 * number6
if answer_multiplication == answer_multiplication_2:
    print("The answer is correct")
else:
    print("The answer is wrong")

print()

# Division
number7 = random.randint(0, 99)
number8 = random.randint(0, 99)

answer_division = eval(input("What is " + str(number7) + "/" + str(number8) + " = "))
answer_division_2 = number7 / number8
answer_division_3 = round(answer_division_2, 2)
if answer_division == answer_division_2:
    print("The answer is correct")
elif number8 == 0:
    print("The divisor should not be equal to 0")
else:
    print("The answer is wrong")
