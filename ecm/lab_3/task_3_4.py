from functools import reduce

def hamming_distance(genome_1, genome_2):
    return reduce(lambda x, y: x + 1 if not len(set(y)) == 1 else x, zip(genome_1, genome_2), 0)

def number_to_pattern(index, k):
    b = ''
    while index > 0:
        b = str(index % 4) + b
        index = index // 4
    dict_rep = {'0': 'A', '1': 'C', '2': 'G', '3': 'T'}
    return ''.join([dict_rep[s] for s in b.zfill(k)])

def reverse_complement(dna):
    dict_rep = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(list(reversed([dict_rep[n] for n in dna])))

def approximate_frequent_words(text, k, d):
    counters = [[number_to_pattern(i, k), 0] for i in range(4 ** k)]

    for i in range(len(text) - k + 1):
        substr = text[i:i + k]
        inv_substr = reverse_complement(substr)

        for pattern in counters:

            if hamming_distance(substr, pattern[0]) <= d:
                pattern[1] += 1

            if hamming_distance(inv_substr, pattern[0]) <= d:
                pattern[1] += 1

    max_value = max(counters, key=lambda pattern: pattern[1])[1]
    return map(lambda x: x[0], filter(lambda pattern: pattern[1] == max_value, counters))

print(*approximate_frequent_words(input(), *list(map(int, input().split()))))