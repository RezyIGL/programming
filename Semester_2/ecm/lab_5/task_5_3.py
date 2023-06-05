def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def neighbours(pattern, d):
    if d == 0:
        return set(pattern)
    if len(pattern) == 1 and d > 0:
        return {'A', 'C', 'G', 'T'}

    neighborhood = set()
    suffix = pattern[1:]
    suffix_neighbors = neighbours(suffix, d)
    for neighbour in suffix_neighbors:
        if hamming_distance(suffix, neighbour) < d:
            neighborhood.update({l + neighbour for l in {'A', 'C', 'G', 'T'}})
        else:
            neighborhood.update({pattern[0] + neighbour})
    return neighborhood


def pattern_to_number(dna):
    dna = dna.replace("A", "0").replace("C", "1").replace("T", "3").replace("G", "2")
    dna = int(dna, 4)
    return dna


def number_to_pattern(index, k):
    conv = ''
    while index > 0:
        conv = "ACGT"[index % 4] + conv
        index = index // 4
    return "A" * (k - len(conv)) + conv


def frequent_words_in_list_with_sorting(lst, k):
    index = [pattern_to_number(word) for word in lst]
    index.sort()
    len_sorted = len(index)
    count = [0] * len_sorted
    for i in range(len_sorted):
        if index[i] == index[i - 1]:
            count[i] = count[i - 1] + 1
        else:
            count[i] = 1
    max_count = max(count)
    frequent_patterns = list(map(lambda sub: number_to_pattern(sub, k),
                                 [index[i] for i, count in enumerate(count) if count == max_count]))
    return frequent_patterns


def frequent_words_with_mismatches(text, k, d):
    lent = len(text)
    index = [text[i:i + k] for i in range(lent - k + 1)]
    sosedi = [nb for sub in index for nb in neighbours(sub, d)]
    return frequent_words_in_list_with_sorting(sosedi, k)

text = input()
k, d = map(int, input().split())
print(*frequent_words_with_mismatches(text, k, d))