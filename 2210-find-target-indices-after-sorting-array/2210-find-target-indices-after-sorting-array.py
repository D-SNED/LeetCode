class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        res = []

        for i in range(len(nums)):
            if nums[i] > target:
                break
            elif nums[i] < target:
                continue
            else:
                res.append(i)

        return res
