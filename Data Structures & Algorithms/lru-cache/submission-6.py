class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.left = Node() # repersents least recently used
        self.right = Node() # repersents most recently used
        self.left.next = self.right 
        self.right.prev= self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache[key].val
        self.add(key, val)
        return val

    def put(self, key: int, val: int) -> None:
        self.add(key, val)
        if len(self.cache) > self.capacity:
            self.remove(self.left.next.key)
        

    def add(self, key, val):
        self.remove(key)
        self.cache[key] = Node(key, val, self.right.prev, self.right)
        self.right.prev.next = self.cache[key]
        self.right.prev = self.cache[key]
            
    def remove(self, key):
        if key not in self.cache:
            return
        self.cache[key].prev.next, self.cache[key].next.prev = self.cache[key].next, self.cache[key].prev
        del self.cache[key] 


    """

    cache = {1: (1, 10, L, R), 2: (2, 20, 1, R)}
    capacity = 2
    L <> 2 <> 3 <> R
    L <> 1  <> 2 <> R
    


            Input:
        ["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

        Output:
        [null, null, 10, null, null, 20, -1]

        Explanation:
        LRUCache lRUCache = new LRUCache(2);
        lRUCache.put(1, 10);  // cache: {1=10}
        lRUCache.get(1);      // return 10
        lRUCache.put(2, 20);  // cache: {1=10, 2=20}
        lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
        lRUCache.get(2);      // returns 20 
        lRUCache.get(1);      // return -1 (not found)
    """