# calculator.py
class Calculator:
    def add(self, a, b):
        """Add two numbers and return the result."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a and return the result."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers and return the result."""
        return a * b
    
    def divide(self, a, b):
        """Divide a by b and return the result.
        
        Raises:
            ZeroDivisionError: If b is 0.
        """
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return a / b
    
    def power(self, a, b):
        """Raise a to the power of b and return the result."""
        return a ** b