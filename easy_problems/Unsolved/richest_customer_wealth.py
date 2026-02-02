class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        # You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer 
        # has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
        wealth = 0

        for x in range(0, len(accounts)):
            subtotal = 0
            for y in range(len(accounts[x])):
                subtotal += accounts[x][y]
            if subtotal > wealth:
                wealth = subtotal
            subtotal = 0
        
        return wealth
    

sol = Solution()
accounts = [[1,5],[7,3],[3,5]] # Output = 10
print(sol.maximumWealth(accounts))