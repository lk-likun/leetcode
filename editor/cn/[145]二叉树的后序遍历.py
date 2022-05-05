# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def Traversal(subroot):
            if not subroot:
                return
            Traversal(subroot.left)
            Traversal(subroot.right)
            res.append(subroot.val)

        res = []
        Traversal(root)
        return res

# leetcode submit region end(Prohibit modification and deletion)
