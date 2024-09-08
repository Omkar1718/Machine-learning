def simple_intrest(p, n, r):
    """
    This function takes following inputs
    p = Principal in INR
    n = Number of years
    r = Rate of Intrest in %p.a.
    Output = Intrest and amount
    """
    I = (p*n*r)/100
    A = p + I
    return I, A