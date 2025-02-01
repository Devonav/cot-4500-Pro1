import math
# Define the functions for the numerical methods in Assignment 1
def approximation_algorithm(x: float, n: int) -> float:
    """Approximates a function using a given series expansion."""
    result = 0.0
    for i in range(n):
        result += (-1)**i * (x ** (2*i)) / math.factorial(2*i)  # Example: cosine approximation
    return result
#bisection method is used to find the root of a function
def bisection_method(f, a: float, b: float, tol: float = 1e-6) -> float:
    """Finds root of function f in [a, b] using the Bisection Method."""
    if f(a) * f(b) >= 0:
        raise ValueError("Function values at the interval endpoints must have opposite signs.")
    
    while (b - a) / 2 > tol:
        midpoint = (a + b) / 2
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2
#fixed point iteration is used to find the root of a function
def fixed_point_iteration(g, x0: float, tol: float = 1e-6, max_iter: int = 100) -> float:
    """Finds root using Fixed-Point Iteration method."""
    x = x0
    for _ in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("Fixed-Point Iteration did not converge within max iterations.")
#newton raphson method is used to find the root of a function
def newton_raphson(f, df, x0: float, tol: float = 1e-6, max_iter: int = 100) -> float:
    """Finds root using Newton-Raphson method."""
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            return x
        if dfx == 0:
            raise ValueError("Derivative is zero. Newton-Raphson method fails.")
        x = x - fx / dfx
    raise ValueError("Newton-Raphson method did not converge within max iterations.")
# main function to test the functions

if __name__ == "__main__":
    # Example function for manual testing
    f = lambda x: x**3 - x - 2
    df = lambda x: 3*x**2 - 1
    g = lambda x: math.sqrt(x + 2)  # Example for fixed-point iteration
    
    print("Approximation Algorithm:", approximation_algorithm(1.0, 10))
    print("Bisection Method:", bisection_method(f, 1, 2))
    print("Fixed-Point Iteration:", fixed_point_iteration(g, 1.5))
    print("Newton-Raphson Method:", newton_raphson(f, df, 1.5))
