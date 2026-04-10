class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []

        for num in nums:
            arr.append(abs(num))

        res = []

        for num in arr:
            res.append(num ** 2)

        res.sort()

        return res