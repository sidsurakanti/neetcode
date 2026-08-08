class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)

        leftMax = [0] * l
        rightMax = [0] * l
        m = 0
        i = 1
        while i < l:
            m = max(m, height[i-1])
            leftMax[i] = m
            i += 1
            
        m = 0
        j = l - 2
        while j >= 0:
            m = max(m, height[j+1])
            rightMax[j] = m
            j -= 1

        i = c = 0
        while i < l:
            c += max(min(leftMax[i], rightMax[i]) - height[i], 0)
            i += 1

        return c


        
            
