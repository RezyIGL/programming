def hSort(nums: list) -> list:
    gap, temp = nums[0], nums[1]

    for i in range(nums[0], len(temp)):
        elem = temp[i]
        index = i
        while index >= gap and elem < temp[index - gap]:
            temp[index] = temp[index - gap]
            index -= gap
        temp[index] = elem
        yield temp

input = int(input()), list(map(int, input().split()))

for i in hSort(input):
    print(*i)
