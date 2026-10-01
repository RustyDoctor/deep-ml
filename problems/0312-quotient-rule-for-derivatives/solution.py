import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    g1 = sum(n*x**i for i, n in enumerate(reversed(g_coeffs)))
    g2 = sum(n*(i+1)*x**(i) for i, n in enumerate(reversed((g_coeffs[:-1]))))

    h1 = sum(n*x**i for i, n in enumerate(reversed(h_coeffs)))
    h2 = sum(n*(i+1)*x**(i) for i, n in enumerate(reversed((h_coeffs[:-1]))))
    if h1 == 0:
        return -1
    return (g2*h1 - g1*h2)/((h1)**2)