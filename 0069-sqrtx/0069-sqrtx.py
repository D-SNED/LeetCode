class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x

        lo = 1
        hi = x

        while lo <= hi:
            mid = (hi + lo) // 2

            if mid == x // mid:
                return  mid

            elif mid > x // mid:
                hi = mid -1
            else:
                lo = mid + 1
        return hi


            


