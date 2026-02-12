class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        d = {}
        l = 0
        max_f = 0

        for r in range(len(s)):
            d[s[r]] = 1 + d.get(s[r], 0)
            max_f = max(d[s[r]], max_f)

            while (r - l + 1) - max_f > k:
                d[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res

