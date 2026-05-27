class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        seen = set()

        def dfs(node):
            seen.add(node)

            for nei in graph[node]:
                if nei not in seen:
                    dfs(nei)

        connected = 0

        for node in range(n):
            if node not in seen:
                connected += 1
                dfs(node)
                
        return connected

            

            
