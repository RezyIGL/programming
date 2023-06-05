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
    mass = [0] * 4**k
    for i in range(len(text) - k + 1):
        pattern = text[i : i + k]
        num = Pattern_to_Number (pattern)
        mass[num] = mass[num] + 1
    return mass


def Better_Clump_Finding (text, k , t, L):
    result = []
    clump = [False] * (4**k)
    mass = ComputingFrequencies(text[0: L], k)
    for i in range (4**k):
        if mass[i] >= t:
            clump[i] = True
        else:
            clump[i] = False
    for i in range (1, len(text) - L):
        prefNum = Pattern_to_Number(text[i - 1 : i + k - 1])
        suffNum = Pattern_to_Number(text[i + L - k : i + L])
        mass[prefNum] -= 1
        mass[suffNum] += 1
        if mass[suffNum] >= t:
            clump[suffNum] = True
    for i in range (4**k):
        if clump[i]:
            result.append(Number_to_Pattern(i, k))
    return result


a = input ()
b = list(map(int, input().split()))
print (*Better_Clump_Finding (a, b[0] , b[2], b[1]))