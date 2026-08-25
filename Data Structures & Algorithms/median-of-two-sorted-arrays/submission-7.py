class Solution:
    def findMedianSortedArrays(self, n1: List[int], n2: List[int]) -> float:
        # two pointers (no extra space)
        n, m = len(n1), len(n2)
        curr = prev = 0

        k = (n + m) // 2 + 1
        i = j = 0
        while i + j < k:
            prev = curr
            if j > m - 1 or (i < n and n1[i] <= n2[j]):
                curr = n1[i]
                i += 1
            else:
                curr = n2[j]
                j += 1
            # print(prev, curr)

        if n + m & 1:
            return curr
        else:
            return (prev + curr) / 2

