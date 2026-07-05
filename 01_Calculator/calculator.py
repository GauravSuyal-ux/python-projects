# ==========================================
# Project: Simple Calculator
# Author: Gaurav Suyal
# Description: A menu-driven calculator
# ==========================================

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b


def modules(a,b):
    if b == 0:
        return "Error ! Cannot divide by zero."
    return a % b

def exponent(a,b):
    return a**b

def menu():
    print("\n========== SIMPLE CALCULATOR ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modules")
    print("6. Exponent")
    print("7. Exit")


while True:

    menu()

    choice = input("Enter your choice (1-7): ")

    if choice == "7":
        print("\nThank you for using the calculator!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice! Please try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers!")
        continue

    if choice == "1":
        print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")

    elif choice == "2":
        print(f"\nResult: {num1} - {num2} = {subtract(num1, num2)}")

    elif choice == "3":
        print(f"\nResult: {num1} * {num2} = {multiply(num1, num2)}")

    elif choice == "4":
        print(f"\nResult: {num1} / {num2} = {divide(num1, num2)}")

    elif choice == "5":
        print(f"\nResult: {num1} % {num2} = {modules(num1,num2)}")

    elif choice == "6":
        print (f"Result: {num1} ** {num2} = {exponent(num1,num2)}")