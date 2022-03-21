class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 1;
        save_flag = 1;
        last_unique = nums[0];
        for i in range(len(nums)):
            if nums[i] != last_unique:
                result += 1
                last_unique = nums[i]
                temp = nums[i]
                nums[i] = nums[save_flag]
                nums[save_flag] = temp 
                save_flag += 1 
                
        return result, nums