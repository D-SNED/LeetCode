class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        
        for digit in digits:
            s += str(digit)
            
        s = int(s) + 1
        
        s = str(s)
        
        a = []
        
        for c in s:
            a.append(int(c))
            
        return a
        
        