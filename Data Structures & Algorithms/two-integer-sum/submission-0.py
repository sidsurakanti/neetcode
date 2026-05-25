class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i in range(len(nums)):
            k = nums[i]
            if target - k in seen:
                return [seen[target-k], i]
            seen[k] = i
