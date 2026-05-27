class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {char: set() for word in words for char in word}
        indegree = {char: 0 for char in graph}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break
            
        q = deque()

        for char in indegree:
            if indegree[char] == 0:
                q.append(char)

        res = []

        while q:
            char = q.popleft()
            res.append(char)

            for nei in graph[char]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)
        
        if len(res) != len(indegree):
            return ""
        
        return "".join(res)
                
            
            
        
                