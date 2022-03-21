# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def get_list(self, root):
        if root == None:
            return 
        self.get_list(root.left)
        self.list.append(root.val)
        self.get_list(root.right)
        
    def binary_search(self, target, start, end):
        middle = (start + end) // 2
        if start > end:
            return False
        if self.list[middle] == target:
            return True 
        elif self.list[middle] > target:
            return self.binary_search(target, start, middle - 1)
        else: 
            return self.binary_search(target, middle + 1, end)
        
    
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.list = []
        self.get_list(root)
        for i in range(len(self.list)):
            num = self.list[i]
            if (k % 2 == 0) and num == (k // 2):
                if i > 0 and self.list[i - 1] == num:
                    return True 
                if i < len(self.list) - 1 and self.list[i + 1] == num:
                    return True 
            else:
                other = k - num 
                if self.binary_search(other, 0, len(self.list) - 1):
                    return True 
                         
        