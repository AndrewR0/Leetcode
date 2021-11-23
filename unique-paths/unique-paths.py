class Solution:
    def uniquePaths(self, m: int, n: int, check = {}) -> int:
        
        key = f'{m},{n}'
        
        if key in check:
            return check[key]        
        if m == 1 and n == 1:
            return 1
        if m == 0 or n == 0:
            return 0
        check[key] = self.uniquePaths(m-1,n,check) + self.uniquePaths(m, n-1,check)
        return check[key]