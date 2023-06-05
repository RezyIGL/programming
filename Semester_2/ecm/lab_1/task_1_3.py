text = input()
k = input()

def Count(Text, Pattern):
    cnt = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i+len(Pattern)] == Pattern:
            cnt += 1
    return cnt

def genAllPatterns(text, k):
    Patterns = set()
    for i in range(len(text) - int(k) + 1):
        Patterns.add(text[i:i+int(k)])
    return Patterns

def printer(text, k):
    returnString = ""
    returnMass = []
    maxR = 0
    for i in genAllPatterns(text, k):
        if Count(text, i) > maxR:
            maxR = Count(text, i)
    for n in genAllPatterns(text, k):
        if Count(text, n) == maxR:
            returnMass.append(n)
    returnMass.sort()
    for i in returnMass:
        returnString += f"{i} "
    return returnString

print(printer(text, k))