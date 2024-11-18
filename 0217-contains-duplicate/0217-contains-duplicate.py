class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _set = set(nums)
        
        return False if len(_set) == len(nums) else True