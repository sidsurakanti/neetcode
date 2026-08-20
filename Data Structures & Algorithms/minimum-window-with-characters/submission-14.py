from collections import defaultdict
import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t: return s

        # sliding window
        l = r = 0
        m = math.inf
        d = defaultdict(int)
        for ch in t:
            d[ch] += 1
        need = len(d.keys())
        have = 0
        window = defaultdict(int)
        sx = ''

        while r < len(s): 
            if have < need:
                # print(l, r)
                new_ch = s[r]
                
                if new_ch in t:
                    window[new_ch] += 1
                    if window[new_ch] == d[new_ch]:
                        have += 1
                # print(new_ch, r, have, need)
                r += 1
            else: # have == need
                if r - l < m:
                    m = r - l
                    sx = s[l:r]
                # print(m, sx)

                # shrink window
                old_ch = s[l]
                l += 1
                if old_ch in t:
                    window[old_ch] -= 1
                    if window[old_ch] < d[old_ch]:
                        have -= 1
        
        while have == need:
            if r - l < m:
                m = r - l
                sx = s[l:r]
            # print(m, sx)

            # shrink window
            old_ch = s[l]
            l += 1
            if old_ch in t:
                window[old_ch] -= 1
                if window[old_ch] < d[old_ch]:
                    have -= 1
            

        return sx


        




        # brute force
        n = len(s)
        m = math.inf
        sx = ''
        d = defaultdict(int)

        for ch in t:
            d[ch] += 1

        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                dx = defaultdict(int)
                for ch in substring:
                    if ch in t:
                        dx[ch] += 1

                # count if t in s:
                if d == dx and len(substring) < m:
                    m = len(substring)
                    sx = substring
        
        return sx
                    

        

            
                


