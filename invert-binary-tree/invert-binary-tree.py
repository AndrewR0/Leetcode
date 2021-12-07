# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        
        right, left = root.right, root.left
        root.right, root.left = left, right
        
        self.invertTree(root.right)
        self.invertTree(root.left)
        
        '''
        
        right = root.right
        left = root.left

        root.left = right
        root.right = left

        self.invertTree(root.left)
        self.invertTree(root.right)
        '''
        
        return root