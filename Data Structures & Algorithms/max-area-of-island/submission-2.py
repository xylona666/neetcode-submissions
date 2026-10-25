class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int: # 多了统计dfs的count并且全局统计max——count
        r = len(grid)
        c = len(grid[0])
        visited = set()
        self.maxcount = 0
        def dfs(i,j):
            if i>=0 and j>=0 and i<r and j<c and (i,j) not in visited:
                if grid[i][j] == 1: # 三个条件缺一不可
                    visited.add((i,j))
                    return 1+dfs(i+1,j)+dfs(i,j+1)+dfs(i-1,j)+dfs(i,j-1)
            return 0
        for i in range(r):
            for j in range(c):
                if (i,j) in visited or grid[i][j] == 0:
                    continue
                
                count = dfs(i,j)

                self.maxcount = max(count,self.maxcount)

        return self.maxcount

                

    