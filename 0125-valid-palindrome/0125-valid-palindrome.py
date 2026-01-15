class Solution:
    def isPalindrome(self, s: str) -> bool:
        # change char to lowercase
        # remove non alphanumerics

        res = ""

        for char in s:
            if char.isalnum():
                res += char.lower()

        return res == res[::-1]
