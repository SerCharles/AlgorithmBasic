class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        visit = []
        for i in range(len(nums)):
            visit.append(False)
        visit[0] = True 
        for i in range(1, len(nums)):
            for j in range(0, i):
                if visit[j] == True:
                    if (j + nums[j]) >= i:
                        visit[i] = True 
                        break 
        return visit[len(nums) - 1]