class Solution:
    def getConcatenation(self, nums: int) -> int:
        ans = []
        ans.extend(nums)
        ans.extend(nums)
        return ans