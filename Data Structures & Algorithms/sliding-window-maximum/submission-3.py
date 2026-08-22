from collections import deque
class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        l = r = 0
        res = []
        tr = deque([(a[r], r)])

        while r < len(a):
            ch = a[r]

            # remove if curr max is expired
            if (r - tr[0][1]) == k:
                tr.popleft()

            # scrub maxes smaller than ch bc they will never be used
            # this will mean that tr[0] will always be the max
            i = len(tr) - 1
            while i >= 0 and tr[i][0] <= ch:
                # print('here')
                tr.pop()
                i -= 1
            tr.append((ch, r))

            r += 1
            if r - l == k: # keep window at len k
                res.append(tr[0][0])
                l += 1
        
        return res
                
        

        