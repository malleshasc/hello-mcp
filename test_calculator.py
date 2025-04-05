# test_calculator.py
import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    """Fixture to create a Calculator instance for each test."""
    return Calculator()

def test_add_positive_numbers(calculator):
    """Test addition with positive numbers."""
    assert calculator.add(1, 2) == 3

def test_add_negative_numbers(calculator):
    """Test addition with negative numbers."""
    assert calculator.add(-1, -2) == -3

def test_add_mixed_numbers(calculator):
    """Test addition with mixed positive and negative numbers."""
    assert calculator.add(-1, 2) == 1

def test_add_zero(calculator):
    """Test addition with zero."""
    assert calculator.add(5, 0) == 5

def test_subtract_positive_numbers(calculator):
    """Test subtraction with positive numbers."""
    assert calculator.subtract(5, 3) == 2

def test_subtract_negative_numbers(calculator):
    """Test subtraction with negative numbers."""
    assert calculator.subtract(-5, -3) == -2

def test_subtract_mixed_numbers(calculator):
    """Test subtraction with mixed positive and negative numbers."""
    assert calculator.subtract(5, -3) == 8

def test_subtract_zero(calculator):
    """Test subtraction with zero."""
    assert calculator.subtract(5, 0) == 5

def test_multiply_positive_numbers(calculator):
    """Test multiplication with positive numbers."""
    assert calculator.multiply(2, 3) == 6

def test_multiply_negative_numbers(calculator):
    """Test multiplication with negative numbers."""
    assert calculator.multiply(-2, -3) == 6

def test_multiply_mixed_numbers(calculator):
    """Test multiplication with mixed positive and negative numbers."""
    assert calculator.multiply(-2, 3) == -6

def test_multiply_by_zero(calculator):
    """Test multiplication by zero."""
    assert calculator.multiply(5, 0) == 0

def test_divide_positive_numbers(calculator):
    """Test division with positive numbers."""
    assert calculator.divide(6, 3) == 2

def test_divide_negative_numbers(calculator):
    """Test division with negative numbers."""
    assert calculator.divide(-6, -3) == 2

def test_divide_mixed_numbers(calculator):
    """Test division with mixed positive and negative numbers."""
    assert calculator.divide(-6, 3) == -2

def test_divide_by_zero(calculator):
    """Test division by zero raises appropriate exception."""
    with pytest.raises(ZeroDivisionError):
        calculator.divide(5, 0)

def test_power_positive_base_and_exponent(calculator):
    """Test power with positive base and exponent."""
    assert calculator.power(2, 3) == 8

def test_power_negative_base_positive_exponent(calculator):
    """Test power with negative base and positive exponent."""
    assert calculator.power(-2, 3) == -8

def test_power_zero_exponent(calculator):
    """Test power with any base and zero exponent."""
    assert calculator.power(5, 0) == 1