"""Unit test for calculator library."""

import calculator


class TestCalculator:
    """Test Cases."""

    def test_addition(self):
        """addition."""
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        """substraction."""
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        """mul."""
        assert 100 == calculator.multiply(10, 10)
