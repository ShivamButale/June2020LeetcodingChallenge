class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            i = 0
            for i in range(0, len(nums)):
                if nums[i] > target:
                    return i
                else:
                    pass
            return len(nums)
