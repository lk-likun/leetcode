# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)

    def getDepth(self, node):
        if not node:
            return 0
        leftDepth = self.getDepth(node.left)
        rightDepth = self.getDepth(node.right)
        depth = max(leftDepth, rightDepth) + 1
        return depth
# leetcode submit region end(Prohibit modification and deletion)
