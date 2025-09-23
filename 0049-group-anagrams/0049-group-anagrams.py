class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for word in strs:
            sorted_ = "".join(sorted(word))
            if sorted_ not in d:
                d[sorted_] = []
            d[sorted_].append(word)

        return list(d.values())

        
                
                