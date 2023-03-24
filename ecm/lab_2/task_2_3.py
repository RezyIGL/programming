from collections import defaultdict
import itertools
a = input()
b =  int(input())

def Count(Text, Pattern):
    counter = 0
    for i in range (len(Text)-len(Pattern)+1):
        if Text[i: i+len(Pattern)] == Pattern:
            counter+=1
    return counter

def ComputingFrequencies(genome, k):
    dictionary = defaultdict()
    for i in itertools.product("ACGT", repeat = k):
        dictionary[i] = Count(genome, "".join(i))
    return [i for i in dictionary.values()]

print (*ComputingFrequencies(a, b))