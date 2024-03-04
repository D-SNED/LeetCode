class Solution:
    def reverseWords(self, s: str) -> str:
        split_str = s.split()
        rev = split_str[::-1]
        return " ".join(rev)
        