# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getPaths(self, root, path, res):
        if not root:
            return
        path += str(root.val)
        if not root.left and not root.right:
            res.append(path)
        else:
            path += '->'
            self.getPaths(root.left, path, res)
            self.getPaths(root.right, path, res)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.getPaths(root, '', res)
        return res

# leetcode submit region end(Prohibit modification and deletion)
