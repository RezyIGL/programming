def NaiveBubbleSort(nums: list) -> list:
    temp = nums
    for i in range(len(temp) - 1):
        for j in range(len(temp) - 1):
            if temp[j] > temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]
    return temp

if __name__ == "__main__":
    NaiveBubbleSort()