class InfixToPostfixConverter:
    """Клас для перетворення інфіксного виразу в зворотний польський запис (ЗПЗ)."""
    
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    def __init__(self, expression):
        self.expression = expression
        self.stack = []
        self.output = []
    
    def validate(self):
        """Перевірка на правильність інфіксного виразу."""
        balance = 0
        prev_token = None
        for token in self.expression.replace("(", " ( ").replace(")", " ) ").split():
            if token == '(':
                balance += 1
            elif token == ')':
                balance -= 1
            elif token in self.precedence and (prev_token in self.precedence or prev_token == '('):
                return False  # Неправильне розташування оператора
            elif not token.isdigit() and token not in self.precedence:
                return False  # Не допустимий символ
            prev_token = token
        return balance == 0
    
    def convert(self):
        """Метод для перетворення виразу в ЗПЗ."""
        if not self.validate():
            raise ValueError("Invalid infix expression")
        
        for token in self.expression.replace("(", " ( ").replace(")", " ) ").split():
            if token.isdigit():
                self.output.append(token)
            elif token == '(':
                self.stack.append(token)
            elif token == ')':
                while self.stack[-1] != '(':
                    self.output.append(self.stack.pop())
                self.stack.pop()
            else:  # Оператор
                while self.stack and self.precedence.get(self.stack[-1], 0) >= self.precedence[token]:
                    self.output.append(self.stack.pop())
                self.stack.append(token)
        
        while self.stack:
            self.output.append(self.stack.pop())
        
        return self.output


class PostfixEvaluator:
    """Клас для обчислення виразу в зворотному польському записі (ЗПЗ)."""
    
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else 'Zero Division Error',
        '^': lambda a, b: a ** b,
    }
    
    def __init__(self, postfix_expression):
        self.postfix_expression = postfix_expression
        self.stack = []
    
    def evaluate(self):
        """Метод для обчислення ЗПЗ виразу."""
        for token in self.postfix_expression:
            if token.isdigit():
                self.stack.append(int(token))
            else:
                b, a = self.stack.pop(), self.stack.pop()
                result = self.operations[token](a, b)
                if result == 'Zero Division Error':
                    return result
                self.stack.append(result)
        return self.stack[0]


class ExpressionEvaluator:
    """Клас для повного обчислення виразу від інфіксної форми до результату."""
    
    def __init__(self, expression):
        self.expression = expression
    
    def evaluate(self):
        # Перетворюємо інфіксну форму в ЗПЗ
        converter = InfixToPostfixConverter(self.expression)
        try:
            postfix_expression = converter.convert()
        except ValueError as e:
            return str(e)
        
        # Виводимо ЗПЗ
        print("Postfix expression:", ' '.join(postfix_expression))
        
        # Обчислюємо результат ЗПЗ
        evaluator = PostfixEvaluator(postfix_expression)
        result = evaluator.evaluate()
        return result


# Приклад використання
if __name__ == "__main__":
    expression = input("Enter an infix expression: ")
    evaluator = ExpressionEvaluator(expression)
    result = evaluator.evaluate()
    print(f"Result: {result}")
