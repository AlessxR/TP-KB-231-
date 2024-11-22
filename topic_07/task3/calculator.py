import logging
from operations import Operations
from util import checkOper

# Налаштування логування
logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Calculator:
    def __init__(self):
        self.result = None  # Змінна для зберігання результату обчислення

    def perform_operation(self, num1, num2, operation):
        if operation == "+":
            return Operations.add(num1, num2)
        elif operation == "-":
            return Operations.subtract(num1, num2)
        elif operation == "*":
            return Operations.multiply(num1, num2)
        elif operation == "/":
            return Operations.divide(num1, num2)

    def get_number(self, prompt):
        """Отримати число від користувача з перевіркою."""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Помилка: введіть коректне число.")

    def get_operation(self):
        """Отримати операцію від користувача з перевіркою."""
        while True:
            operation = input("Введіть операцію (+, -, *, /): ")
            if checkOper(operation):
                return operation
            print("Помилка: некоректна операція. Спробуйте ще раз.")

    def calc(self):
        """Головний цикл калькулятора."""
        logging.info("Calculator started.")

        print("Калькулятор запущено (введіть 'exit', щоб вийти).")
        
        while True:
            # Запит на завершення програми
            expression = input("Введіть 'exit', щоб вийти, або натисніть Enter, щоб продовжити: ").lower()
            if expression == "exit":
                logging.info("Calculator exited.")
                print("Вихід...")
                break

            # Отримання першого числа
            num1 = self.get_number("Введіть перше число: ")
            logging.info(f"First number entered: {num1}")


            # Отримання операції
            operation = self.get_operation()
            logging.info(f"Operation selected: {operation}")


            # Отримання другого числа
            num2 = self.get_number("Введіть друге число: ")
            logging.info(f"Second number entered: {num2}")

            # Виконання обчислення
            self.result = self.perform_operation(num1, num2, operation)
            logging.info(f"Calculation result: {num1} {operation} {num2} = {self.result}")
            # Виведення результату
            print(f"Результат: {self.result}")

