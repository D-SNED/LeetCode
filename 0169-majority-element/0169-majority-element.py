class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = Counter(nums)

        for num in nums:
            if d[num] > len(nums) // 2:
                return num