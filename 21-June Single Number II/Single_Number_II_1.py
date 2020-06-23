class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        msp = defaultdict(int)
        for i in nums:
            msp[i] = nums.count(i)
            if msp[i] == 1:
                return i
