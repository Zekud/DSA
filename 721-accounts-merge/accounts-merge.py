class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        def find(x):
            if x != parent.setdefault(x,x):
                parent[x] = find(parent[x])
            return parent[x]        
        def union(x,y):
            parent[find(x)] = find(y)

        email_to_name = {}
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                union(first_email,email)
                email_to_name[email] = name
        groups = defaultdict(list)
        for email in email_to_name:
            root = find(email)
            groups[root].append(email)
        res = []
        for root in groups:
            res.append([email_to_name[root]] + sorted(groups[root]))
        return res
