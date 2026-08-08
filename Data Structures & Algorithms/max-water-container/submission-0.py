class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        m = 0

        while i < j:
            x = heights[i]
            print(j)
            y = heights[j]
            m = max(m, min(x, y)*(j-i))

            if x < y:
                i += 1
            else:
                j -= 1
        
        return m

