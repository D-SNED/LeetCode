class Solution:
    def reverseWords(self, s: str) -> str:
        split_str = s.split()
        return " ".join(reversed(split_str))
        