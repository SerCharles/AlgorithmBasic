class Solution(object):
    def judge_sum(self, nums, target, start_position, multiply, current_result):
        current_result = current_result + multiply * nums[start_position]
        start_position += 1
        if start_position == len(nums):
            if current_result == target:
                self.sum += 1
            return 
        self.judge_sum(nums, target, start_position, 1, current_result)
        self.judge_sum(nums, target, start_position, -1, current_result)

    
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.sum = 0    
        self.judge_sum(nums, target, 0, 1, 0)
        self.judge_sum(nums, target, 0, -1, 0)
        return self.sum
    
    
a = Solution()
a.findTargetSumWays([1, 1, 1, 1, 1], 3)