class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def r(start, n, a):
            if n > target or start >= len(nums):
                return 
            elif n == target:
                return res.append(a)
            else:
                for i in range(start, len(nums)):
                    r(i, n + nums[i], a + [nums[i]])

        r(0, 0, [])
        return res
            
                