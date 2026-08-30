class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cmax = i = 0
        gmax = -float("infinity")

        while i < len(nums):
            if cmax < 0:
                cmax = nums[i]
            else:
                cmax += nums[i]
            gmax = max(cmax, gmax)
            i += 1
            
        return gmax
