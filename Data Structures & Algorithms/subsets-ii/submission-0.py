class Solution:
    def subsetsWithDup(self, n: List[int]) -> List[List[int]]:
        ret = []
        n = sorted(n)
        def solve(arr, k):
            if k == len(n):
                # if not arr in ret:
                ret.append(arr)
                return
            solve(arr + [n[k]], k + 1)
            # skip tree levels until we're past dupes
            while k + 1 < len(n) and n[k+1] == n[k]:
                k += 1
            solve(arr, k + 1) # wo choosing curr number

        solve([], 0)
        return ret

            