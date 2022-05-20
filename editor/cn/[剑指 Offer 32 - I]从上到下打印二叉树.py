# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        res = []

        def helper(subroot, depth):
            if not subroot:
                return []
            if len(res) == depth:
                res.append([])
            res[depth].append(subroot.val)
            if subroot.left:
                helper(subroot.left, depth + 1)
            if subroot.right:
                helper(subroot.right, depth + 1)

        helper(root, 0)
        return sum(res, [])
# leetcode submit region end(Prohibit modification and deletion)
