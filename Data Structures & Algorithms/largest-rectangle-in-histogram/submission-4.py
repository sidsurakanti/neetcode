from collections import deque
class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        stk = deque()
        i = 0
        max_area = 0

        while i < len(h):
            left_idx = i # smallest i

            # add every ele greater than smallest
            # & clear everything thats bigger than curr from stack
            while stk and stk[-1][0] > h[i]: # worst case < n
                val, idx = stk.pop()
                left_idx = min(left_idx, idx)

                # compute max area of this height before popping
                a = val * (i - idx)
                max_area = max(max_area, a) 
            else:
                stk.append((h[i], left_idx))
            i += 1

        # print(stk)
        
        # atp the stack will have all the remaining blocks
        # that never encounter a smaller block after
        for v, idx in stk:
            a = (len(h) - idx) * v
            max_area = max(a, max_area)

        return max_area
