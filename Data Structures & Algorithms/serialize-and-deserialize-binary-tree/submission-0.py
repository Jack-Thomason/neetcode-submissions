# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        queue = deque([root])
        res = []

        while queue:
            node = queue.popleft()

            if not node:
                res.append("$")    
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        ans = ",".join(res)
        print(ans)
        return ans
            
                
        
        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        vals = data.split(",")

        if vals[0] == "$":
            return None

        root = TreeNode(int(vals[0]))

        q = deque([root])
        i = 1

        while q and i < len(vals):
            node = q.popleft()

            if i < len(vals) and vals[i] != "$":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1

            if i < len(vals) and vals[i] != "$":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        
        return root
                

