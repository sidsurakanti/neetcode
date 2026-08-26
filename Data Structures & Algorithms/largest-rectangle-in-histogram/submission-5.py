class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        stack = []
        i = max_area = 0

        for i, v in enumerate(h):
            left_idx = i # min possible i (how far this h can stretch left)

            # add every ele greater than smallest (stk[0])
            # & clear everything thats bigger than curr from stack
            while stack and stack[-1][0] > v: # worst case < n
                val, idx = stack.pop()
                left_idx = min(left_idx, idx)

                # compute max area of this height before popping
                a = val * (i - idx)
                max_area = max(max_area, a) 
            else:
                stack.append((h[i], left_idx))
        # atp the stack will have all the remaining blocks
        # that never encounter a smaller block after
        for v, i in stack:
            a = (len(h) - i) * v
            max_area = max(a, max_area)

        return max_area
