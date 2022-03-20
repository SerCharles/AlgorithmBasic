class Solution(object):
    def binarysearch(self, nums, target, start, end):
        if start > end: 
            return -1        
        middle = (start + end) // 2 
        if nums[middle] == target:
            return middle 
        elif nums[middle] < target:
            return self.binarysearch(nums, target, middle + 1, end)
        else: 
            return self.binarysearch(nums, target, start, middle - 1)
    
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarysearch(nums, target, 0, len(nums) - 1)
        