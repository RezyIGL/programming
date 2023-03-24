from functools import reduce

def hamming_distance(genome_1, genome_2):
    return reduce(lambda x, y: x + 1 if not len(set(y)) == 1 else x, zip(genome_1, genome_2), 0)

def func(pattern, text, d):
    result = []
    for i in range(len(text)-len(pattern)+1):
        s = text[i:i+len(pattern)]
        if hamming_distance(s, pattern) <= d:
            result.append(i)
    return result
print(*func(input(),input(),int(input())))