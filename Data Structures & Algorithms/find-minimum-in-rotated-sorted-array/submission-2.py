class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        if r == 0:
            return nums[0]

        # go right until we find a number smaller than previous
        # then go left until the next number is bigger

        while l <= r:
            k = (l + r) // 2
            print(k)

            if nums[k+1] < nums[k] and nums[k-1] < nums[k]: # [5, 6, 1]
                return nums[k+1]
            elif nums[-1] > nums[k]:
                # go left
                r = k - 1
            else:
                l = k + 1
        
        return nums[l]
            


