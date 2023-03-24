def pattern_to_number(dna):
    dna = dna.replace("A", "0").replace("C", "1").replace("T", "3").replace("G", "2")
    return int(dna, 4)


def number_to_pattern(index, k):
    conv = ''
    while index > 0:
        conv = "ACGT"[index % 4] + conv
        index = index // 4
    return "A" * (k - len(conv)) + conv


def frequent_words_with_sorting(text, k):
    lent = len(text)
    index = [pattern_to_number(text[i:i + k]) for i in range(lent - k + 1)]
    sorted_index = sorted(index)
    len_sorted = len(sorted_index)
    count = [0] * len_sorted
    for i in range(len_sorted):
        if sorted_index[i] == sorted_index[i - 1]:
            count[i] = count[i - 1] + 1
        else:
            count[i] = 1
    max_count = max(count)
    frequent_patterns = list(map(lambda sub: number_to_pattern(sub, k),
                                 [sorted_index[i] for i, count in enumerate(count) if count == max_count]))
    return count, frequent_patterns


text = input()
k = int(input())
print(*frequent_words_with_sorting(text, k)[0])
print(*frequent_words_with_sorting(text, k)[1])