class Calculator:
    def add(self, num1: int, num2: int):
        return num1 + num2

    def subtract(self, num1: int, num2: int):
        return num1 - num2

    def multiply(self, num1: int, num2: int):
        return num1 * num2

    def divide(self, num1: int, num2: int):
        if (num2 == 0):
            raise ZeroDivisionError
        return num1/num2

