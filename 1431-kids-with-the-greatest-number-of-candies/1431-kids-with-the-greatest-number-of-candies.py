class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []

        max_before_candies = max(candies)

        for amount in candies:
            if amount + extraCandies < max_before_candies:
                res.append(False)
            else:
                res.append(True)
        
        return res