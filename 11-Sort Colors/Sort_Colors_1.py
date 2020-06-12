class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #0,1,2, red, white, blue
        r = 0
        w = 0
        b = len(nums)-1
            
        while w <= b:
            if nums[w] == 0:
                nums[r], nums[w] = nums[w], nums[r]
                w += 1
                r += 1
            elif nums[w] == 2:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1
            else:  
                w += 1
        
