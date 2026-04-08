class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = {}

        td = {}

        for char in s:
            sd[char] = 1 + sd.get(char, 0)
        for char in t:
            td[char] = 1 + td.get(char, 0)

        return sd == td