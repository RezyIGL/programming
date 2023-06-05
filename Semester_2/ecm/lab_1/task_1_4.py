text = input()
def ReverseComplement(dna):
    revString = ""
    dictionary = {"A": "T", "T": "A", "C":"G", "G":"C"}
    for let in dna:
        revString += dictionary[let]
    return revString[::-1]
print(ReverseComplement(text))