class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return []
        nums.sort()
        ret = [[i] for i in nums]
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    if len(ret[i]) < len(ret[j]) + 1:
                        ret[i] = ret[j] + [nums[i]]
        return max(ret, key=len)
