class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited =set()
        r = len(grid)
        c = len(grid[0])
        count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]=="1" :
                    if (i,j) in visited:
                        continue
                    else:
                        def dfs(i,j):
                            if i>=0 and j>=0 and i<r and j<c and (i,j) not in visited:
                                if grid[i][j]=="1":
                                    visited.add((i,j)) # 这样怎么表
                                    dfs(i+1,j) 
                                    dfs(i,j+1)
                                    dfs(i-1,j)
                                    dfs(i,j-1)
                            return
                        dfs(i,j)
                        count +=1

        
        return count
                    




