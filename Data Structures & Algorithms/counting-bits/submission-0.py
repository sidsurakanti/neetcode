class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for k in range(n+1):
            c = 0
            while k != 0:
                k &= k - 1
                c += 1
            res.append(c)


        return res