import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    g_x = np.polyval(g_coeffs, x)
    h_x = np.polyval(h_coeffs, x)

    g_prime_x = np.polyval(np.polyder(g_coeffs), x)
    h_prime_x = np.polyval(np.polyder(h_coeffs), x)

    return float((g_prime_x * h_x - g_x * h_prime_x) / (h_x**2))


   