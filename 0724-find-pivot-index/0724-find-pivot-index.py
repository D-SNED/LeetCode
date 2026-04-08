class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left_sum = 0

        for i in range(len(nums)):
            right_sum = sum(nums) - nums[i] - left_sum
            if left_sum == right_sum:
                return i
            left_sum += nums[i]

        return -1

