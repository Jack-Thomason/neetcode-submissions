# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_order_map = {value: idx for idx, value in enumerate(inorder)}

        preorder_index = 0


        def helper(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            root_val = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_val)

            in_order_index = in_order_map[root_val]

            root.left = helper(left, in_order_index - 1)
            root.right = helper(in_order_index + 1, right)

            return root

        return helper(0, len(inorder) - 1)
            