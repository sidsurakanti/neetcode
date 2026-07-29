class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i, j = 0, len(s1)

        s1c = [0]*26
        for c in s1:
            s1c[ord(c) - ord('a')] += 1
        
        s2c = [0]*26
        for c in s2[0:j]:
            s2c[ord(c) - ord('a')] += 1

        while True:
            if s2c == s1c: return True
            if j >= len(s2):
                break
            
            s2c[ord(s2[i]) - ord('a')] -= 1
            s2c[ord(s2[j]) - ord('a')] += 1
            i += 1
            j += 1
        
        return False
