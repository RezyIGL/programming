def pow(x: float, n: int) -> float:
    p = 1
    if n < 0:
        x = 1 / x
        n = abs(n)

    while n:
        if n % 2:
            p *= x
        x *= x
        n //= 2
    return p


if __name__ == "__main__":
    x = 2.0
    n = -4
    print(pow(x, n))
