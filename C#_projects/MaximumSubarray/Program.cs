public class Solution {
    public static int MaxSubArray(int[] nums) {
        int maxEnding = nums[0];
        int max = nums[0];
        
        for (int i = 1; i < nums.Length; i++)
        {
            maxEnding = Math.Max(nums[i], maxEnding + nums[i]);
            max = Math.Max(max, maxEnding);
        }

        return max;
    }

    public static void Main()
    {
        Console.WriteLine(MaxSubArray(new int[] { 0, 1, 2, -1, -2, 3, 4, -1, 5 })); // 11
    }
}