# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        current = root

        if not current:
            return None
        
        l = self.invertTree(current.right)
        r = self.invertTree(current.left)
        current.left = l
        current.right = r

        return current


    


    

        