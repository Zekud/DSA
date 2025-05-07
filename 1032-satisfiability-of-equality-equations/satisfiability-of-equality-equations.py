class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        root = {} 
        def find(x):
            if x != root.setdefault(x,x):
                root[x] = find(root[x])
            return root[x]

        def union(x,y):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return 

            root[rooty] = rootx
        def get(x,y):
            return find(x) == find(y)
        for eq in equations:
            if eq[1] == "=":
                x = eq[0]
                y = eq[3]
                union(x,y)
        for eq in equations:
            if eq[1] == "!":
                x = eq[0]
                y = eq[3]
                if get(x,y):
                    return False
        return True