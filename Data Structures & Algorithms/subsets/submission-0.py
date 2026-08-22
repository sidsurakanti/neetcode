class Solution:
    def subsets(self, n: List[int]) -> List[List[int]]:
        ret = []
        def solve(arr, k):
            if k == len(n):
                ret.append(arr)
                return
            solve(arr, k + 1) # wo choosing curr number
            solve(arr + [n[k]], k + 1)
        solve([], 0)
        return ret

            
