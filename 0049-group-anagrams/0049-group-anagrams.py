class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for string in strs:
            sorted_word = "".join(sorted(string))
            
            if sorted_word not in d:
                d[sorted_word] = []
            d[sorted_word].append(string)
            
        return list(d.values())
                
                