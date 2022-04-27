# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 迭代
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#         stack = [root]
#         result = []
#         while stack:
#             node = stack.pop()
#             result.append(node.val)
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)
#         return result
# 递归
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []

        def Traversal(subroot):
            if not subroot:
                return
            order.append(subroot.val)
            Traversal(subroot.left)
            Traversal(subroot.right)

        Traversal(root)
        return order

# leetcode submit region end(Prohibit modification and deletion)
