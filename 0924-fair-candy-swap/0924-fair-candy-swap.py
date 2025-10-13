class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:

        target = (sum(aliceSizes) - sum(bobSizes)) // 2
        aliceSizes = set(aliceSizes)

        for size in set(bobSizes):
            if target + size in aliceSizes:
                return [target + size, size]