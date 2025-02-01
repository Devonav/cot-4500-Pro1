import unittest
import math
# Import the functions to test
from src.main.assignment_1 import approximation_algorithm, bisection_method, fixed_point_iteration, newton_raphson
# Define the test class for the numerical methods in Assignment 1 
class TestNumericalMethods(unittest.TestCase):
    # test the approximation algorithm
    def test_approximation_algorithm(self):
        """Test the approximation algorithm (e.g., cosine series expansion)."""
        x = 0  # cos(0) should be 1
        result = approximation_algorithm(x, 10)
        print(f"Approximation Algorithm Output: {result}")
        self.assertAlmostEqual(result, 1.0, places=5)
# test the bisection method
    def test_bisection_method(self):
        """Test the bisection method on x^3 - x - 2 = 0 (root near x = 1.521)."""
        f = lambda x: x**3 - x - 2
        root = bisection_method(f, 1, 2)
        print(f"Bisection Method Output: {root}")
        self.assertAlmostEqual(root, 1.521, places=3)
#test the fixed point iteration
    def test_fixed_point_iteration(self):
        """Test the fixed-point iteration method with a transformed function."""
        g = lambda x: math.sqrt(x + 2)  # Derived from x = sqrt(x + 2)
        root = fixed_point_iteration(g, 1.5)
        expected_value = math.sqrt(root + 2)
        print(f"Fixed-Point Iteration Output: {root}")
        self.assertAlmostEqual(root, expected_value, places=5)
#test the newton raphson method
    def test_newton_raphson(self):
        """Test the Newton-Raphson method on x^3 - x - 2 = 0 (root near x = 1.521)."""
        f = lambda x: x**3 - x - 2
        df = lambda x: 3*x**2 - 1
        root = newton_raphson(f, df, 1.5)
        print(f"Newton-Raphson Method Output: {root}")
        self.assertAlmostEqual(root, 1.521, places=3)

if __name__ == "__main__":
    unittest.main()
