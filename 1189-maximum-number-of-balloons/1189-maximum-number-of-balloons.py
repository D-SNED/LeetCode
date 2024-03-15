class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        map_t = Counter(text)
        map_b = Counter("balloon")
        
        res = len(text)
        for c in map_b:
            res = min(res, map_t[c] // map_b[c])
        return res
            
        
        
        
        
        
        
        
            
                
                
        
                    
                    