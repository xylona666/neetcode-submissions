class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        while l <= r:
            mid_speed = (l+r)//2
            time = 0
            for i in piles:
                if i%mid_speed == 0:
                    time += i//mid_speed
                else:
                    time += i//mid_speed+1
             

            if time <= h:
                r = mid_speed-1 # 这个边界值怎么考虑
            elif time > h :
                l = mid_speed+1
        return l