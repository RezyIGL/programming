def PatternToNumber(dna): return int(dna.replace("A", "0").replace("C", "1").replace("G", "2").replace("T", "3"), 4)
print(PatternToNumber(input()))