dna = input()
def CountNucleotides(dna):
    dictionary = {"A": dna.count("A"), "C": dna.count("C"), "G": dna.count("G"), "T": dna.count("T")}
    return "{} {} {} {}".format(dictionary["A"], dictionary["C"], dictionary["G"], dictionary["T"])
print(CountNucleotides(dna))