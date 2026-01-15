class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        max_f = 0

        d = {}

        for r in range(len(s)):
            d[s[r]] = 1 + d.get(s[r], 0)
            max_f = max(max_f, d[s[r]])

            while (r - l + 1) - max_f > k:
                d[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res