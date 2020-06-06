class Solution:

    def __init__(self, w: List[int]):
        self.w = w[:]
        for i in range(1, len(self.w)):
            self.w[i] += self.w[i-1]                 

    def pickIndex(self) -> int:
        index = random.randint(1, self.w[-1])
        ret, low, high = -1, 0, len(self.w) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if self.w[mid] >= index:
                ret = mid
                high = mid - 1
            else:
                low = mid + 1
        return ret        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
