
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # for i in range(len(nums) - 2):
        #     for j in range(i, len(nums) -1):
        #         for k in range(j, len(nums)):
        #             if nums[i] < nums[j] < nums[k]:
        #                 return True
        # return False
        
        first = second = float("inf")
        
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False