# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# 1   2   3   4   5
# F   F   F   T   T

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        hi = n

        while lo < hi:
            mid = (lo + hi) // 2
            if isBadVersion(mid):
                hi = mid
            else: 
                lo = mid + 1 
        return lo

    