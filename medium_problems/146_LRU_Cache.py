class LRUCache:

    def __init__(self, capacity: int):
        #initializes
        return 0

    def get(self, key: int) -> int:
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.buckets:
            self.buckets[key] = value
        else:
            # Test for capacity overriding
            return 
    