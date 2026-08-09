class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        q = []
        res = [0] * (l:=len(t))

        for i in range(l):
            while len(q) > 0 and t[q[-1]] < t[i]:
                k = q.pop()
                res[k] = i-k
            q.append(i)
        return res