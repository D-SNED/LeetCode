class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        d = {}
        l = 0

        for r in range(len(fruits)):
            d[fruits[r]] = 1 + d.get(fruits[r] , 0)

            if len(d) > 2:
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    d.pop(fruits[l])
                l += 1
            
            res = max(res, r - l + 1)

        return res