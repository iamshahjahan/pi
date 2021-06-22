from lru_cache import LRUCache

if __name__ == "__main__":
    lru = LRUCache()
    lru.put(1, "Shahjahan")
    lru.put(2, "a")
    lru.put(3, "b")
    print(lru.get(1))
    lru.put(5, "d")
    lru.put(4, "f")
    lru.put(6, "e")



    print(lru)
