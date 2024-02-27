class Solution:
    def sortVowels(self, s: str) -> str:
        ref = "AEIOUaeiou"
        index = 0
        _store = []
        
        l = list(s)
        
        for i in range(len(l)):
            if l[i] in ref:
                _store.append(l[i])
                l[i] = "*"
                
        _store = sorted(_store)
                
        for i in range(len(l)):
            if l[i] == "*":
                l[i] = _store[index]
                index += 1
            
        return "".join(l)
        
    
            
        