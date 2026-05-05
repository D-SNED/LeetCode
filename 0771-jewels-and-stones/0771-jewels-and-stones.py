class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0

        stones_d = Counter(stones)

        _set = set(jewels)

        for char in _set:
            if char in stones_d:
                res += stones_d[char]

        return res