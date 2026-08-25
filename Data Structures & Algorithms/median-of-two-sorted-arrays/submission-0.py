class Solution:
    def findMedianSortedArrays(self, n1: List[int], n2: List[int]) -> float:
        # brute force
        merged = []
        i, j = 0, 0

        while i < len(n1) and j < len(n2):
            if (a := n1[i]) <= (b := n2[j]):
                merged.append(a)
                i += 1
            else:
                merged.append(b)
                j += 1
        
        if i < len(n1):
            merged+=(n1[i:])
        else:
            merged+=(n2[j:])
        # print(merged, len(merged) & 1)

        # step 2: get median
        if (l := len(merged)) & 1:
            return merged[l // 2]
        else:
            return (merged[l // 2] + merged[(l // 2) - 1])/2
        