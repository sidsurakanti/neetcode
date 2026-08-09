class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1]
        s = ([0] * (len(nums) - 1)) + [1]

        for i in range(1, len(nums)):
            p.append(nums[i-1] * p[i-1])
            
        for i in range(len(nums)-2, -1, -1):
            s[i] = nums[i+1] * s[i+1]


        return [p[i]*s[i] for i in range(len(nums))]


        