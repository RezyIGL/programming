# It must be in-place
def reverseString(stroke: list) -> None:
    for i in range(len(s)//2):
        s[i], s[-i-1] = s[-i-1], s[i]

s = ["h", "e", "l", "l", "o"] # ["o", "l", "l", "e", "h"] 
reverseString(s); print(s)