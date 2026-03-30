class MyHashMap:

    def __init__(self):
        self.bucket_count = 1000
        self.buckets = [[] for _ in range(self.bucket_count)]

    def put(self, key: int, value: int) -> None:
        bucket_num = key % self.bucket_count
        for i in range(len(self.buckets[bucket_num])):
            old_key, old_value = self.buckets[bucket_num][i]

            if old_key == key:
                self.buckets[bucket_num][i] = (key,value)
                return
        self.buckets[bucket_num].append((key,value))

    def get(self, key: int) -> int:
        bucket_num = key % self.bucket_count

        for old_key,old_value in self.buckets[bucket_num]:
            if old_key == key:
                return old_value
        return -1

    def remove(self, key: int) -> None:
        bucket_num = key % self.bucket_count
        for i in range(len(self.buckets[bucket_num])):
            old_key, old_value = self.buckets[bucket_num][i]

            if old_key == key:
                self.buckets[bucket_num].pop(i)
                return
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)