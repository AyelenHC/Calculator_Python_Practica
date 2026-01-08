# Create class Calculator
class Calculator:

    def __init__(self):
        """
            Constructor of the Calculator class
        """
        self.num1 = 1
        self.num2 = 0
        self.subtotal = 0
    
    def getSubtotal(self):
        """
            Get the subtotal
            Returns: the subtotal
        """
        return self.subtotal

    def add(self, num1, num2):
        """
            Add two numbers and return the subtotal
            Args:
                num1: the first number
                num2: the second number
            Returns: the subtotal the addition of the two numbers
        """
        self.subtotal = round(num1 + num2, 10)
        return self.subtotal

    def subtract(self, num1, num2):
        """
            Subtract two numbers and return the subtotal
            Args:
                num1: the first number
                num2: the second number
            Returns: the subtotal the subtraction of the two numbers
        """

        self.subtotal = round(num1 - num2, 10)
        return self.subtotal

    def multiply(self, num1, num2):
        """
            Multiply two numbers and return the subtotal
            Args:
                num1: the first number
                num2: the second number
            Returns: the subtotal the multiplication of the two numbers
        """
        self.subtotal = round(num1 * num2, 10)
        return self.subtotal

    def divide(self, num1, num2):
        """
            Divide two numbers and return the subtotal
            Args:
                num1: the first number
                num2: the second number
            Returns: the subtotal the division of the two numbers

            Raises: ZeroDivisionError if the second number is zero
            Returns: None if the second number is zero
        """
        if num2 == 0:
            return None

        return round(num1 / num2, 10) # presion a 10 decimales

    def clear(self):
        """
            Clear the subtotal
        """
        self.subtotal = 0
        self.setNum1(0)
        self.setNum2(0)
    
    def setNum1(self, num):
        self.num1 = num
    
    def setNum2(self, num):
        self.num2 = num

    def getNum1(self):
        return self.num1
    
    def getNum2(self):
        return self.num2
