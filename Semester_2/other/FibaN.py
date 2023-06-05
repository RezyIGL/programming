def Fiba(n: int) -> int:
    sqr5 = 5**0.5
    f1 = (1 + sqr5)/2
    f2 = (1 - sqr5)/2
    formula = (f1**n - f2**n) // sqr5
    return int( formula )

print(Fiba(1_000_000))