pattern = input()
text = input()
def PatternMatching(Text, Pattern):
    retArr = []
    retStr = ""
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i+len(Pattern)] == Pattern:
            retArr.append(i)
    retArr.sort()
    for i in retArr:
        retStr += f"{i} "
    return retStr
print(PatternMatching(text, pattern))