import math

def approximation_algorithm(x, n):
    """Approximates a value using the Taylor Series expansion."""
    result = 0
    for i in range(n):
        result += ((-1)**i * (x**(2*i+1))) / math.factorial(2*i+1)
    return result

def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    """Finds the root of func using the Bisection Method."""
    if func(a) * func(b) >= 0:
        raise ValueError("Function values at a and b must have opposite signs.")

    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(func(c)) < tol or (b - a) / 2 < tol:
            return c
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
    return c

def fixed_point_iteration(g, x0, tol=1e-6, max_iter=100):
    """Solves x = g(x) using Fixed-Point Iteration."""
    x = x0
    for _ in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

def newton_raphson_method(func, deriv, x0, tol=1e-6, max_iter=100):
    """Finds the root of func using Newton-Raphson Method."""
    x = x0
    for _ in range(max_iter):
        f_x = func(x)
        f_prime_x = deriv(x)
        if abs(f_x) < tol:
            return x
        if f_prime_x == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x -= f_x / f_prime_x
    return x
