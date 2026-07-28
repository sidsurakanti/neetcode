class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 1


        m = 0
        curr_char = s[0]
        kp = k
        while i < len(s):
            curr_char = s[i]
            
            if j < len(s) and s[j] == curr_char:
                j += 1
            else:
                if kp > 0:
                    kp -= 1
                    j += 1
                else:
                    m = max(m, j - i)
                    i += 1
                    j = i + 1
                    kp = k
        else:
            print(j - i, kp)

            m = max(m, j - i + kp)
        
        m = min(len(s), m)
        
        return m
        

        