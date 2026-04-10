class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cur_max = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                res = max(res, cur_max)
                cur_max = 0
            else:
                cur_max += 1

        return max(res, cur_max)
