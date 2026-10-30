class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs
        quene = deque()
        r = len(grid)
        fresh = 0
        c = len(grid[0])
        for rc in range(r):
            for cc in range(c):
                if grid[rc][cc] == 2:
                    quene.append((rc,cc))
                elif grid[rc][cc] ==1:
                    fresh +=1

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        time = 0 
        while quene and fresh >0:
            
            time +=1
            for _ in range(len(quene)):
                nr,nc = quene.popleft()
                for d1,d2 in directions:
                    cr = d1+nr
                    cc = d2+nc
                    if cc>=0 and cc<c and cr<r and cr>=0 and grid[cr][cc] == 1 :
                        grid[cr][cc] = 2 # 改成2 
                        fresh -=1
                        quene.append((cr,cc))
 
        
        return time if fresh == 0 else -1