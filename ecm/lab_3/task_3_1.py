def MinSkew(genome):
    skews = [None]*(len(genome)+1)
    skews[0] = 0
    for i in range(len(genome)):
        if genome[i] == "G":
            skews[i+1] = skews[i] + 1
        elif genome[i] == "C":
            skews[i+1] = skews[i] - 1
        else:
            skews[i+1] = skews[i]
    min_val = min(skews)
    return [x for x, y in enumerate(skews) if y == min_val]
print(*MinSkew(input()))