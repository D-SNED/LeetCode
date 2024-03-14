class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        i = 0
        
        while i <= len(nums) - 1:
            if nums[i] == val:
                del nums[i]
                nums.append("_")
                count += 1
            else:
                i += 1
            
        return len(nums) - count
        
        
        