class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = len(edges)
        parent = [i for i in range(size + 1)]
        rank = [0] * (size+1)

        def find(x):
            if x != parent[x]:
                parent[x]= find(parent[x])
            return parent[x]
        def union(x,y):
            rootx = find(x)
            rooty = find(y)

            if rootx == rooty:
                return False
            if rank[rootx] > rank[rooty]:
                parent[rooty] = rootx
            elif rank[rooty] > rank[rootx]:
                parent[rootx] = rooty
            else:
                parent[rooty] = rootx
                rank[rootx] +=1
            return True

        for u,v in edges:
            if not union(u,v):
                return [u,v]