class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = Counter(s)
        count_t = Counter(t)

        for char in s:
            if count_t.get(char) != count_s.get(char):
                return False
        return True
