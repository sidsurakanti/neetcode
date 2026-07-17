class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = set()
        for i in range(len(nums)):
            j = 0
            k = len(nums)-1

            while j < k:
                if j == i:
                    j += 1
                    continue
                elif k == i:
                    k -= 1
                    continue
                # i + j + k = 0
                # i = -j -k
                # -i = j + k
                if (a := nums[j]) + (b := nums[k]) == -(c:= nums[i]):
                    triplets.add(tuple(sorted([a, b, c])))
                    k -= 1
                    j += 1
                elif a + b < -c:
                    j += 1
                else: # a + b > -c
                    k -= 1
        
        return list(triplets)

