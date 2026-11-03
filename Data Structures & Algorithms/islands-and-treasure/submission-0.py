class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # 简单的bfs, 转换思维重新排列一下,注意返回值 !!
        if not grid or not grid[0]:
            return
        r = len(grid)
        c = len(grid[0])
        quene = deque()
        dic = [(-1,0),(1,0),(0,1),(0,-1)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    quene.append((i,j))
        count = 0
         
   
        while quene:
            count += 1
            for _ in range(len(quene)):
                cr,cc = quene.popleft() # 0的location
                for i ,j in dic:
                    nr = cr+i
                    nc = cc+j
                    if 0<=nr<r and 0<=nc<c:
                        if grid[nr][nc] == 2147483647:
                            grid[nr][nc] = count
                            quene.append((nr,nc))
 