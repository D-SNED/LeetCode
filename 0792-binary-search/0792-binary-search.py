class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            idx = (lo + hi) // 2
            print(idx)

            if nums[idx] == target:
                return idx
            elif nums[idx] < target:
                lo = idx + 1
            else:
                hi = idx - 1

        return -1