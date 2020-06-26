class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if nums is None:
            return -1
        for i in nums:
            if nums.count(i) != 1:
                return i
