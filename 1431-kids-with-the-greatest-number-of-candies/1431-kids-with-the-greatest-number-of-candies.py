class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []

        max_before_candies = max(candies)

        for amount in candies:
            res.append(amount + extraCandies >= max_before_candies)
                
        
        return res