def sum (a,b):
    return a + b

def substract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b