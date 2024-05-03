class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
            
        maxi = 0
        
        for key in d:
            if d[key] > maxi:
                maxi = d[key]
                
        for key in d:
            if d[key] == maxi:
                return key
                
        