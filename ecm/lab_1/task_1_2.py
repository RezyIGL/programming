text = input()
pattern = input()
def Count(Text, Pattern):
    cnt = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i+len(Pattern)] == Pattern:
            cnt += 1
    return cnt
print(Count(text, pattern))