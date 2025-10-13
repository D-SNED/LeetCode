class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_sum = sum(aliceSizes)
        bob_sum = sum(bobSizes)

        target = (alice_sum - bob_sum) // 2

        for size in bobSizes:
            if target + size in aliceSizes:
                return [target + size, size]