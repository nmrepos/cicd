class Calculator:
    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return a minus b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b
     
    def divide(self, a, b):
        """Return a divided by b, or raise a ValueError if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b