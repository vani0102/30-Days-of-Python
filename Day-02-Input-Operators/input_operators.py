# Day 2 - Input & Operators
# 30 Days of Python

# Topics Covered:
# 1. Taking user input
# 2. Type conversion
# 3. Arithmetic operators
# 4. Comparison operators
# 5. Logical operators
# 6. Assignment operators


# --------------------------------------------------
# 1. Taking User Input
# --------------------------------------------------

name = input("Enter your name: ")
print("Hello", name)


# --------------------------------------------------
# 2. Type Conversion
# --------------------------------------------------

age = int(input("Enter your age: "))
cgpa = float(input("Enter your CGPA: "))

print("Age:", age)
print("CGPA:", cgpa)


# --------------------------------------------------
# 3. Arithmetic Operators
# --------------------------------------------------

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)


# --------------------------------------------------
# 4. Comparison Operators
# --------------------------------------------------

x = 10
y = 20

print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater Than:", x > y)
print("Less Than:", x < y)
print("Greater Than or Equal:", x >= y)
print("Less Than or Equal:", x <= y)


# --------------------------------------------------
# 5. Logical Operators
# --------------------------------------------------

age = 22

print("AND:", age > 18 and age < 30)
print("OR:", age < 18 or age > 20)
print("NOT:", not(age > 18))


# --------------------------------------------------
# 6. Assignment Operators
# --------------------------------------------------

number = 10

number += 5
print("After += :", number)

number -= 3
print("After -= :", number)

number *= 2
print("After *= :", number)

number /= 4
print("After /= :", number)


# --------------------------------------------------
# 7. Practice Problems
# --------------------------------------------------

# Q1. Add two numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)


# Q2. Calculate average of three numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average:", average)


# Q3. Check whether a number is even or odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Q4. Calculate Simple Interest

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)


# Q5. Check eligibility based on age

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
