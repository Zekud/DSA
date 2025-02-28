class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cp = capacity
        self.used = {}
        self.counter = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.used[key] = self.counter
            self.counter +=1
            return self.cache[key]
        else:
            return -1
       

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.used[key] = self.counter
            self.cache[key] = value
            self.counter +=1
        else:
            if len(self.cache) < self.cp:
                self.cache[key] = value
                self.used[key] = self.counter
                self.counter+=1
            else:
                lr= k = float('inf')
                
                for ky in self.used:
                    if self.used[ky] < lr:
                        lr = self.used[ky]
                        k = ky
                del self.used[k]
                del self.cache[k]
                self.cache[key] = value
                self.used[key] = self.counter
                self.counter+=1
                

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)