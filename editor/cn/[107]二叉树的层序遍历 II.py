# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
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
        return res[::-1]
# leetcode submit region end(Prohibit modification and deletion)
