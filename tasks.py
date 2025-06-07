# 1. Variable Tasks

# Task 1: Basic Variables

name = "Snehan S"
age = 18
height = 1.80
likes_python = True

print(f"Name: {name}, Age: {age}, Height: {height}m, Likes Python: {likes_python}")

# Task 2: Variable Swapping

a = 5
b = 10

a += b
b = a - b
a -= b
print(a, b)

# 2. Operator Calculations

# Task 3: Simple Calculator

num1 = 10
num2 = 5

sum = num1 + num2
diff = num1 - num2
product = num1 * num2
div = num1 / num2

print(f"Sum of {num1} and {num2} is: {sum}")
print(f"Difference of {num1} and {num2} is: {diff}")
print(f"Product of {num1} and {num2} is: {product}")
print(f"Division of {num1} by {num2} is: {div}")

# Task 4: Modulus Operation

number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. If Condition Tasks

# Task 5: Age Checker

age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif 13 <= age < 20:
    print("Teen")
else:
    print("Adult")

# Task 6: Password Checker

password = input("Enter your password: ")

if len(password) < 8:
    print("Invalid")
else:
    print("Valid")

# 4. While Loop Tasks
# Task 7: Countdown

countdown = 10
while countdown >= 1:
    print(countdown)
    countdown -= 1
else:
    print("Happy New Year!")

# Task 8: Guessing Game

secret = 5

while True:
    guess = int(input("Guess a number: "))

    if guess == secret:
        print("You Won!")
        break
    elif guess - secret >= 10:
        print(f"Your guess {guess} is too high")
    elif secret - guess >= 10:
        print(f"Your guess {guess} is too low")
    else:
        print(f"Your guess {guess} is too near")

# Task 9: Sum of numbers

total = 0
while True:
    number = int(input("Enter a number: "))
    if number != 0:
        total += number
    if number == 0:
        print(total)
        break

# 5. Combined Tasks

#5 Task 10: Multiplication Table

number = int(input("Enter a number: "))

i = 1

while i <=10:
    print(f"{number}x{i}={number * i}")
    i += 1

# Task 11: Simple ATM

balance = 1000

while True:
    print("Welcome to the ATM")
    print("Enter 1 for Withdrawals")
    print("Enter 2 for Balance Check")
    print("Enter 3 for Deposit")
    print("Enter 4 to Exit")
    option = int(input("Enter your choice: "))

    if option == 1:
        withdrawal = int(input("Enter the amount you want to withdraw: "))
        if withdrawal <= balance:
            balance -= withdrawal
            print("Please Collect your Cash")
            print("Withdrawal Successful")
        else:
            print("Transaction declined due to insufficient balance.")

    elif option == 2:
        print(f"Your account balance is {balance}")
    
    elif option == 3:
        deposit = int(input("Enter the amount you want to deposit: "))
        balance += deposit
        print("Your money is deposited successfully")
    
    elif option == 4:
        print("Thank you for your visit!")
        break
    else:
        print("You have entered an invalid option")
        print("Please, Try again")