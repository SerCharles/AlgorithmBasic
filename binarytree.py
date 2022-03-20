class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def build_binary_tree(self, preorder, inorder, preorder_root, start, end):
        root = preorder[preorder_root]
        length = end - start + 1
        root_place = -1
        for i in range(length):
            if inorder[i + start] == root:
                root_place = i + start
                break 
        left_start = start
        left_end = root_place - 1
        left_length = left_end - left_start + 1
        right_start = root_place + 1
        right_end = end
        right_length = right_end - right_start + 1
        
        subtree = TreeNode(root)
        if left_length > 0:
            left_root = preorder_root + 1
            subtree.left = self.build_binary_tree(preorder, inorder, left_root, left_start, left_end) 
        if right_length > 0:
            right_root = preorder_root + 1 + left_length
            subtree.right = self.build_binary_tree(preorder, inorder, right_root, right_start, right_end)
        
        return subtree
        
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) <= 0:
            return None
        return self.build_binary_tree(preorder, inorder, 0, 0, len(inorder) - 1)
