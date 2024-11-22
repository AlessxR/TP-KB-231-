import logging

logging.basicConfig(
    filename="calculator.log",  # Зберігання логів до файлу.
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

from operations import add, subtract, multiply, divide
from util import checkOper

def calc():
    logging.info("Calculator starting.")
    print("Калькулятор запущено(введіть exit, щоб вийти).")
    while True:

        expression = input("Введіть 'exit', щоб вийти або натисніть Enter, щоб продовжити: ").lower()
        logging.info("New start the program" + "\n")
        if expression == "exit":
            logging.info("Exit the program")
            print("Вихід...")
            break
    
        while True:
            try:
                num1 = float(input("Введіть перше число: "))
                logging.info(f"First number is entered: {num1}")

                break  # Якщо введено правильне число, вийдемо з циклу
            except ValueError:
                print("Помилка: це не число. Спробуйте ще раз.")
        
        while True:  # Цикл для перевірки операції
            operation = input("Введіть операцію (+, -, *, /): ")
            if checkOper(operation):
                logging.info(f"The operation is selected: {operation}")
                break  # Якщо операція правильна, вийдемо з циклу
            else:
                print("Помилка: некоректна операція. Спробуйте ще раз.")

        while True:
            try:
                num2 = float(input("Введіть друге число: "))
                logging.info(f"Second number is entered: {num2}")
                break  # Якщо введено правильне число, вийдемо з циклу
            except ValueError:
                print("Помилка: це не число. Спробуйте ще раз.")

        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
            
        logging.info(f"The result of the operation: {num1} {operation} {num2} = {result}")
        print("Результат =", result)