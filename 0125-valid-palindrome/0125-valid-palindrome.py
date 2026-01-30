class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""

        s = "".join(s)

        for char in s:
            if char.isalnum():
                res += char.lower()

        return res == res[::-1]