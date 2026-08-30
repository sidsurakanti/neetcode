class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        gmax = 0
        checkd = set()

        for n in nums:
            if n in checkd:
                continue
            i = 0
            while n+i in s:
                i += 1
                checkd.add(n+i)
            gmax = max(i, gmax)
        return gmax


        
        