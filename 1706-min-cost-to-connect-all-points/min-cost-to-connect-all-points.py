class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        weight = []
        n = len(points)
        for i in range(n):
            a,b = points[i]
            j = i+1
            while j < n:
                c,d = points[j]
                val = abs(a-c) + abs(b-d)
                weight.append([val,i,j])
                j+=1
       
        parent = [i for i in range(n)]
        size = [1] * (n+1)
        total =0
        def find(x):
            if x!=parent[x]:
                parent[x] = find(parent[x]) 
            return parent[x]
        def union(x,y):
            x_root = find(x)
            y_root = find(y)
       
            if x_root != y_root:
                if size[x_root] < size[y_root]:
                    x_root, y_root = y_root, x_root
                parent[y_root] = x_root
                
                size[x_root] += size[y_root]
        def connected(x,y):
            return find(x) == find(y)
        weight.sort()
        for i in range(len(weight)):
            w,x,y = weight[i]
            if not connected(x, y):
                union(x,y)
                total +=w
        return total
