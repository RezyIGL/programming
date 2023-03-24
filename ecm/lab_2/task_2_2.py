a,b = map(int, input().split())
def int_to_k(q, k):
    n = ""
    while q>0:
        n=str(q%k)+n
        q//=k
    return n
def NumberToPattern(index, k):
    dictionary = {"0":"A", "1": "C", "2": "G", "3":"T"}
    n = int_to_k(index, 4).zfill(k)
    dna = ""
    for i in n:
        dna+=dictionary[i]
    return dna
print (NumberToPattern(a, b))