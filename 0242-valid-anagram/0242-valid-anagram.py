class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sd = {}
        
        td = {}
        
        for char in s:
            if char not in sd:
                sd[char] = 0
            sd[char] += 1
            
        for char in t:
            if char not in td:
                td[char] = 0
            td[char] += 1
            
        return sd == td
            