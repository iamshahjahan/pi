from dll import DLL, Node


class LRUCache:
    def __init__(self):
        self.dll: DLL = DLL()
        self.map = {}
        self.data = {}
        self.cap = 5

    def accessed(self, key):
        if key in self.map:
            node: Node = self.map[key]
            self.dll.remove(node)

        node: Node = self.dll.addFront(key)
        self.map[key] = node

        if len(self.data) > self.cap:
            del self.map[self.dll.tail.val]
            del self.data[self.dll.tail.val]
            self.dll.remove(self.dll.tail)

    def put(self, key, value):
        self.data[key] = value
        self.accessed(key)

    def get(self, key):
        if key not in self.data:
            return None
        self.accessed(key)
        return self.data[key]

    def __repr__(self):
        return f"{self.dll},{self.map},{self.data}"
