class Solution:
    def climbStairs(self, n: int) -> int:
        d = dict()
        d[1], d[2] = 1, 2

        def c(n):
            if n in d.keys():
                return d[n]
            
            s = c(n - 1) + c(n - 2)
            if s not in d.keys():
                d[n] = s
            
            return s 
        return c(n)


        