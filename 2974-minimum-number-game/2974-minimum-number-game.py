class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        lst = []
        
        while len(nums) > 0:
            min1 = min(nums)
            nums.remove(min1)
            min2 = min(nums)
            nums.remove(min2)
            lst.append(min2)
            lst.append(min1)
        
        return lst
        
        