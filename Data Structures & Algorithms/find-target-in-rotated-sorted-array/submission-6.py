class Solution:
    def search(self, a: List[int], target: int) -> int:
        l = 0
        r = len(a) - 1

        # step1: 
        # find if we're in rot or sorted part of arr
        # compare middle value (m) to (last := a[-1])
            # if m < last: sorted else: rot
        while l <= r:
            m = (l + r) // 2
            mid = a[m]
            print(mid, l, r)
            if target == a[m]: return m

            # step2:
            # compare target with m to choose left or right
            if mid < (last := a[-1]): # sorted part
                print("sorted")
                if target > mid:
                    if target <= last:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    r = m - 1
            else: # in rot part
                if target < mid:
                    if target <= last: l = m + 1
                    else: r = m - 1
                else: # target > m: 
                    l = m + 1 # right
               
        return -1
        


