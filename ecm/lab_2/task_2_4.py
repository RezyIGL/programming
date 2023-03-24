def Number_to_Pattern (num, k):
    dictionary = {"0": "A", "1": "C", "2": "G", "3": "T"}
    if k == 1:
        return dictionary[str(num)]
    q = num // 4
    r = num % 4
    return Number_to_Pattern(q, k-1) + dictionary[str(r)]


def Pattern_to_Number (text):
    dictionary = {"A": "0", "C": "1", "G": "2", "T": "3"}
    if len(text) == 0:
        return 0
    chr = text[-1]
    text  = text[:-1]
    return Pattern_to_Number(text) * 4 + int(dictionary[chr])
    
    
def ComputingFrequencies(text, k):
    mass = [0] * 4 ** k
    for i in range(len(text) - k + 1):
        pattern = text[i : i + k]
        num = Pattern_to_Number (pattern)
        mass[num] = mass[num] + 1
    return mass


def FasterFrequentWords(text, k):
    result = []
    mass = ComputingFrequencies(text, k)
    maxx = max(mass)
    for i in range (4 ** k - 1):
        if mass[i] == maxx:
            pattern = Number_to_Pattern(i, k)
            result.append(pattern)
    return result

print (*FasterFrequentWords(input(), int(input())))