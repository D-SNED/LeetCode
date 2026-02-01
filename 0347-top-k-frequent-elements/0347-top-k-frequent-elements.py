class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            d[num] = 1 + d.get(num, 0)


        d_vals = sorted(list(d.values()))

        max_o = d_vals[-1:-k - 1:-1]

        res = []

        for key in d:
            if d[key] in max_o:
                res.append(key)

        return res
        
        