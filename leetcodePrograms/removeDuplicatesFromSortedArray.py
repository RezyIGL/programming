def removeDuplicates(nums: list) -> int:
    for i in range(len(nums)-1):
        aboba = nums[i]
        while aboba in nums:
            nums.remove(nums[i])
        nums.insert(i, aboba)
    return len(nums), nums

print(removeDuplicates([1, 1, 2]))