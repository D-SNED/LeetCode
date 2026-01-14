class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}

        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in d:
                d[sorted_string] = []
            d[sorted_string].append(string)

        return list(d.values())