class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        self.count = 0
        visited = set()
        dic = {i:[] for i in range(n)}
        for a,b in edges:
            dic[a].append(b)
            dic[b].append(a)
        def dfs(node):
            
                
            for i in dic[node]:
                if i not in visited:
                    visited.add(i)
                    dfs(i)
            return
        for i in range(n):
            if i not in visited:
                
                self.count +=1  
                dfs(i)
        return self.count
                