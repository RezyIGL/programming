nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square = lambda x: x**2
cube = lambda x: x**3

summ = lambda x, y: x + y 
mults = lambda x, y: x * y

from functools import reduce
print(f"""
The sum is: {reduce(summ, nums)}
And the multiplies are: {reduce(mults, nums)}
""")

print("Squares: ")
print(*list(map(square, nums)))

print("\nCubes: ")
print(*list(map(cube, nums)))
