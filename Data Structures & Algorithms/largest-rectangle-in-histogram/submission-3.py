from collections import deque
class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        stk = deque()
        i = 0
        max_area = 0

        while i < len(h):
            smallest = i # smallest i
            while stk and stk[-1][0] > h[i]: # worst case < n
                val, mi = stk.pop()
                a = val * (i - mi)
                max_area = max(max_area, a)
                smallest = min(smallest, mi)
            else:
                stk.append((h[i], smallest))
            # print(stk)

            i += 1
        
        # print(stk)
        for v, idx in stk:
            # calculate area 
            a = (i - idx) * v
            # print(a)
            max_area = max(a, max_area)

        return max_area
            

            
            
            

            


