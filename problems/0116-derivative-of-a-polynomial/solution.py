def poly_term_derivative(c: float, x: float, n: float) -> float:
    if c == 0 or n==0:
        return 0.0
    if n==1:
        return float(c)
    return (n*c*(x**(n-1)))