#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username.upper() == "ADMIN" and password == "12345":
        print("Access granted")
    else:
        print("Access denied")
def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature <=65:
        return "It's a little chilly out there!"
    elif temperature <= 85:
        return "Perfect!"
    else: 
        return "It's too dang hot out there!"

def fizzbuzz(num):
    # your code here
    if num % 5 == 0 and num % 3 ==0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 ==0:
        return "Buzz"
    else:
        return num

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1+num2
    elif operation == "-":
        return num1-num2
    elif operation == "*":
        return num1*num2
    elif operation == "/":
        return num1/num2
    else:
        return "Invalid operation"
