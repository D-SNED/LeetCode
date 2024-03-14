class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        
        for i in range(len(s)):
            if s[i] not in d1:
                d1[s[i]] = [i]
            else:
                d1[s[i]].append(i)
                
        for i in range(len(t)):
            if t[i] not in d2:
                d2[t[i]] = [i]
            else:
                d2[t[i]].append(i)
                
        res1 = []
        res2 = []
        
        for key in d1:
            res1.append(d1[key])
            
        for key in d2:
            res2.append(d2[key])
            
        return res1 == res2
                
        
        
            
        