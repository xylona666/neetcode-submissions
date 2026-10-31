class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs
        # 重新写!multi注意, rc表达符号注意,特殊情况注意,quene pop的方向注意
        r = len(grid)
        c = len(grid[0])
        quene = deque()
        fresh = 0
        time =0 
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    fresh +=1
                elif grid[i][j] == 2:
                    quene.append((i,j)) # rotten numbers
        while quene and fresh>0:
            time +=1
            for _ in range(len(quene)):
                cr,cc = quene.popleft() # rotten number
                for i,j in direction:
        
                    nr = i+cr
                    nc = j+cc
                 
                 
                    if 0<=nr<r and 0<=nc<c and fresh > 0:
                        if grid[nr][nc] == 1: # neighbor
                            print(nr,nc)
                            grid[nr][nc] = 2
                            quene.append((nr,nc))
                            fresh -=1
                
        return time if fresh == 0 else -1



