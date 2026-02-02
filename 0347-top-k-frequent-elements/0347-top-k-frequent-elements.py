import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            d[num] = 1 + d.get(num, 0)

        arr = []

        for num, count in d.items():
            arr.append([count, num])

        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])

        return res


        
        
        