class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d = defaultdict(list)

        for u, v in edges:
            d[u].append(v)
            d[v].append(u)

        def dfs(node):
            if node == destination:
                return True
            for neighbour in d[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    if dfs(neighbour):
                        return True

            return False

        seen = set()
        seen.add(source)

        return dfs(source)