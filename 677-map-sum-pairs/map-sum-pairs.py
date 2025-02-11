class MapSum:

    def __init__(self):
        self.hashmp = {}

    def insert(self, key: str, val: int) -> None:
        self.hashmp[key]= val

    def sum(self, prefix: str) -> int:
        tot =0
        for key in self.hashmp:
            if key.startswith(prefix):
                tot+=self.hashmp[key]
        return tot


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)