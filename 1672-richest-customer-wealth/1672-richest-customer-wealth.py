class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0

        for account in accounts:
            account_sum = sum(account)

            if account_sum > max_wealth:
                max_wealth = account_sum

        return max_wealth