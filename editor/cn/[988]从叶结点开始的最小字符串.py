# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ls = list()

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.dfs(root, "")
        return min(self.ls)

    def dfs(self, root, temp):
        if not root:
            return
        if not root.left and not root.right:
            temp += chr(root.val + 97)
            self.ls.append(temp[::-1])
        self.dfs(root.left, temp + chr(root.val + 97))
        self.dfs(root.right, temp + chr(root.val + 97))

# leetcode submit region end(Prohibit modification and deletion)
