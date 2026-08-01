class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:

        wealth = 0
        for x in range(0, len(accounts)):
            subtotal = 0
            for y in range(len(accounts[x])):
                subtotal += accounts[x][y]
            wealth = max(wealth, subtotal)
            subtotal = 0
        return wealth
    