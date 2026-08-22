class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        l = r = 0
        res = []

        tr = [(a[r], r)]
        timer = 0

        # brute force O(nk)
        while r < len(a):
            ch = a[r]

            if (r - tr[0][1]) == k:
                tr = tr[1:]

            i = len(tr) - 1
            # print(i, tr)
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
                
        

        