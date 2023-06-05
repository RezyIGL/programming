from functools import reduce
def HammingDistance(t1, t2):
    return reduce(lambda cnt, text: cnt + 1 if not len(set(text)) == 1 else cnt, zip(t1, t2), 0)
print(HammingDistance(input(), input()))
