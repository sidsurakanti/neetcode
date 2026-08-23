class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            k = 0

            while n > 0:
                k += (n % 10)**2
                n //= 10
            if k in seen:
                return False
            n = k
            print(k)
            seen.add(n)
        return True

        