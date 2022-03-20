class Solution(object):
    def qsort(self, nums, start, end):
        if start > end:
            return
        pivot = nums[end]
        smaller_place = start - 1
        for i in range(start, end):
            if nums[i] < pivot: 
                smaller_place += 1
                temp = nums[smaller_place]
                nums[smaller_place] = nums[i]
                nums[i] = temp 
                
        smaller_place += 1
        temp = nums[smaller_place]
        nums[smaller_place] = nums[end]
        nums[end] = temp
        self.qsort(nums, start, smaller_place - 1)
        self.qsort(nums, smaller_place + 1, end)  
    
    
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        self.qsort(nums, 0, length - 1)
        print(nums)
        result = []
        for i in range(length):
            if nums[i] == target:
                result.append(i)
        return result

        
        