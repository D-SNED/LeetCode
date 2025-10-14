class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        i = 0

        while i < len(arr1):
            valid = True
            for num in arr2:
                if abs(arr1[i] - num) <= d:
                    valid = False
                    break
            
            if valid:
                res += 1
            i += 1

        return res
            