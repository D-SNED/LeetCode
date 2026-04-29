class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        res = 0
        d = {}

        for num in nums:
            d[num] = 1 + d.get(num, 0)

        for key, value in d.items():
            if value == 1:
                res += key

        return res


