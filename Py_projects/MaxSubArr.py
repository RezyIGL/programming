def Solution(nums: list) -> int:
    mxTail = nums[0]
    mx = nums[0]
    
    for i in range(len(nums)):
        mxTail = max(nums[i], nums[i] + mxTail)
        mx = max(mx, mxTail)
    
    return mx

if __name__ == "__main__":
    print(Solution([0, 1, 2, -1, 3, 4, -1, 5]))