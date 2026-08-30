class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def r(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                
            for c in nums:
                if c not in cur:
                    cur.append(c)
                    r(cur)
                    cur.pop()
        
        r([])
        return res
