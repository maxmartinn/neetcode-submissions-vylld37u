class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = defaultdict(list)
        chars = set("".join(words))
        res = []
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            for j in range(min(len(w1), (len(w2)))):
                if w1[j] != w2[j]:
                    adjList[w1[j]].append(w2[j])
                    break
            else:
                if len(w1) > len(w2):
                    return ""
        
        visit = dict()

        def dfs(c):
            if c in visit:
                return visit[c]

            visit[c] = True
            for nei in adjList[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)
            return False


        for c in chars:
            if dfs(c):
                return ""
        
        return "".join(reversed(res))