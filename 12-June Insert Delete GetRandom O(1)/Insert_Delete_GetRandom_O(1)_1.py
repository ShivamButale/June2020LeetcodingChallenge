class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sett = set()        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.sett:
            return False
        self.sett.add(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.sett:
            self.sett.remove(val)
            return True
        return False
    
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        x = random.randint(0, len(self.sett)-1)
        l = list(self.sett)
        return l[x]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
