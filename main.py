class Calculator():
    def __init__(self, num1=0 , num2=0):
        self.num1 = num1
        self.num2 = num2

    def plus(self, newNum1, newNum2):
        try:
            self.num1 = int(newNum1)
            self.num2 = int(newNum2)
            return self.num1 + self.num2
        except:
            return "Incorrect Input"

    def minus(self, newNum1, newNum2):
        try:
            self.num1 = int(newNum1)
            self.num2 = int(newNum2)
            return self.num1 - self.num2
        except:
            return "Incorrect Input"

    def multiply(self, newNum1, newNum2):
        try:
            self.num1 = int(newNum1)
            self.num2 = int(newNum2)
            return self.num1 * self.num2
        except:
            return "Incorrect Input"

    def divide(self, newNum1, newNum2):
        try:
            self.num1 = int(newNum1)
            self.num2 = int(newNum2)
            return self.num1 / self.num2
        except:
            return "Incorrect Input"

# calculator = Calculator()
# print(calculator.plus(1, 2))
# calculator.minus(5, 3)
# calculator.multiply(3, 4)
# calculator.divide(10, 2)
