class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()

        res = []

        for num in nums:
            if num not in res:
                res.append(num)

        if len(res) < 3:
            return res[-1]
        else:
            return res[-3]