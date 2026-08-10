class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2

            counter = sum([(i + mid - 1) // mid for i in piles])

            if counter > h:
                left = mid + 1
            elif counter <= h:
                right = mid - 1

        return left

