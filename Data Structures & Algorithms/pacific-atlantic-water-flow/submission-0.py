class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #六个问题自己改,平常自己写的时候需要先把思路梳理清楚
        leftorup = []
        dic = [(1,0),(-1,0),(0,-1),(0,1)]
        rl = len(heights) # 错误一
        cl = len(heights[0])
        visited_leup = set()
        visited_bd = set()
        def dfs(r,c,visited):
            cur_h = heights[r][c] # ? 这个怎么out of
            for i,j in dic:
                cr = r+i
                cc = c+j
                if (cr,cc) in visited:
                    continue
                elif 0<=cr<rl and 0<=cc<cl : 
                    if heights[cr][cc] >= cur_h:
                        if  visited == visited_leup:
                            visited_leup.add((cr,cc))
                            dfs(cr,cc,visited_leup)
                        if visited == visited_bd:
                            visited_bd.add((cr,cc))
                            dfs(cr,cc,visited_bd)
            return
 
        for i in range(0,rl):
            visited_leup.add((i,0))
            visited_bd.add((i,cl-1))
            dfs(i,0,visited_leup)
            dfs(i,cl-1,visited_bd)

        for j in range(0,cl):
            visited_leup.add((0,j))
            visited_bd.add((rl-1,j))
            dfs(0,j,visited_leup)
            dfs(rl-1,j,visited_bd)
     
        result = []
        for i in visited_leup:
            if i in visited_bd:
                result.append(i)
        return  result

