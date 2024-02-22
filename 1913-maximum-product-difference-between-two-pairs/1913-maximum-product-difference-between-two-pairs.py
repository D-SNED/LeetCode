class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            min_index = i
            
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
                    
            if i != min_index:
                nums[i], nums[min_index] = nums[min_index], nums[i]
                
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])