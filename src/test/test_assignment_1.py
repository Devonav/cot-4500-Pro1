import unittest
import math
from src.main.assignment_1 import approximation_algorithm, bisection_method, fixed_point_iteration, newton_raphson_method

class TestAssignment1(unittest.TestCase):
    
    def test_approximation_algorithm(self):
        result = approximation_algorithm(math.pi/4, 10)
        print(f"Approximation Algorithm Output: {result}")
        self.assertAlmostEqual(result, math.sin(math.pi/4), places=5)

    def test_bisection_method(self):
        result = bisection_method(lambda x: x**2 - 4, 1, 3)
        print(f"Bisection Method Output: {result}")
        self.assertAlmostEqual(result, 2, places=5)

    def test_fixed_point_iteration(self):
        result = fixed_point_iteration(lambda x: (x + 2/x) / 2, 1)
        print(f"Fixed-Point Iteration Output: {result}")
        self.assertAlmostEqual(result, math.sqrt(2), places=5)

    def test_newton_raphson_method(self):
        result = newton_raphson_method(lambda x: x**2 - 4, lambda x: 2*x, 3)
        print(f"Newton-Raphson Method Output: {result}")
        self.assertAlmostEqual(result, 2, places=5)

if __name__ == '__main__':
    unittest.main()
