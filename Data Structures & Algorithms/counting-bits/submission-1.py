class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for k in range(n+1):
            c = 0
            while k != 0:
                k &= k - 1 # lowest 1 bit in k will be 0 after (k-1)
                c += 1 # clears a set bit each turn so we can js count how many
            res.append(c)


        return res