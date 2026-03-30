class MyHashSet:

    def __init__(self):
        self.list1 = []
        

    def add(self, key: int) -> None:
        if key not in self.list1:
            self.list1.append(key)

        

    def remove(self, key: int) -> None:
        if key in self.list1:
            self.list1.remove(key)

        

    def contains(self, key: int) -> bool:
        return key in self.list1
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)