def SelectSort(nums: list) -> list:
    temp = nums
    for i in range(len(temp)-1):
        j = temp.index(min(temp[i:]))
        temp[i], temp[j] = temp[j], temp[i]
    return temp

input = list(map(int, input().split()))

if __name__ == "__main__":
    SelectSort(input)    
