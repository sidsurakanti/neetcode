class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # cars adj at dest are fleet
        # pos order must not change at dest
        # 
        # attempt 1:
        # sort pos to find first in line
        # find when (t) first in line reaches dest
        # for each car in line check if's t > t+1 if so it creates a new fleet

        cars = sorted(zip(position, speed), reverse=True, key=lambda x: x[0])
        m = 0
        count = 0

        for x, v in cars:
            t = (target - x) / v
            if t > m:
                count += 1
                m = t
        
        return count
            



        