class MyHashSet:

    def __init__(self):
        self.bucket_count = 1000
        self.buckets = [[] for _ in range(self.bucket_count)]
        

    def add(self, key: int) -> None:
        bucket_num = key % self.bucket_count
        if key not in self.buckets[bucket_num]:
            self.buckets[bucket_num].append(key)

    def remove(self, key: int) -> None:
        bucket_num = key % self.bucket_count
        if key in self.buckets[bucket_num]:
            self.buckets[bucket_num].remove(key) 

        
    def contains(self, key: int) -> bool:
        bucket_num = key % self.bucket_count
        return key in self.buckets[bucket_num] 



        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)