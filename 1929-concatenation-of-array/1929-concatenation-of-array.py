class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        
        for i in range(2 * n):
            res.append(nums[i - n])
        return res
            