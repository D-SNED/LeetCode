class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def expone(power):
            if 2 ** power == n:
                return True
            
            if 2 ** power > n:
                return False
            
            new_power = power + 1
            
            return expone(new_power)
        return expone(0)