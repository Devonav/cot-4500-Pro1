import unittest
from src.main.assignment_1 import approximation_algorithm, bisection_method, fixed_point_iteration, newton_raphson_method

class TestAssignment1(unittest.TestCase):
    
    def test_approximation_algorithm(self):
        self.assertAlmostEqual(approximation_algorithm(math.pi/4, 10), math.sin(math.pi/4), places=5)

    def test_bisection_method(self):
        self.assertAlmostEqual(bisection_method(lambda x: x**2 - 4, 1, 3), 2, places=5)

    def test_fixed_point_iteration(self):
        self.assertAlmostEqual(fixed_point_iteration(lambda x: (x + 2/x) / 2, 1), math.sqrt(2), places=5)

    def test_newton_raphson_method(self):
        self.assertAlmostEqual(newton_raphson_method(lambda x: x**2 - 4, lambda x: 2*x, 3), 2, places=5)

if __name__ == '__main__':
    unittest.main()
