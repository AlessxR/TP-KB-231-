def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "На нуль ділити не можна"

def checkOper(operation):
    return operation in "+-*/"

def calc():
    while True:
        expression = input("Введіть 'exit' для виходу з программи або будь-яке число: ")
        if expression.lower() == "exit":
            print("вихід")
            break
        
        num1 = float(expression)
        operation = input("Введіть операцію (+, -, *, /): ")
        
        if not checkOper(operation):
            print("Неправильна операція")
            continue
        
        num2 = float(input("Введіть друге число: "))
        
        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)

        print("Result =", result)

calc()
