# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def Traversal(subroot, order):
            if not subroot:
                return
            Traversal(subroot.left, order)
            order.append(subroot.val)
            Traversal(subroot.right, order)

        order = []
        Traversal(root, order)
        return order
# leetcode submit region end(Prohibit modification and deletion)
