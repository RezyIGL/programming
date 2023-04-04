def TwoSum(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
nums = [2, 5, 5, 11]
target = 10

print(TwoSum(nums, target)) # [1, 2]