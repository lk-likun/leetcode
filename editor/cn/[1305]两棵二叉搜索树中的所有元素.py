# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def Traversal(subroot, res):
            if not subroot:
                return
            res.append(subroot.val)
            Traversal(subroot.left, res)
            Traversal(subroot.right, res)

        res1 = []
        res2 = []
        Traversal(root1, res1)
        Traversal(root2, res2)
        return sorted(res1 + res2)

# leetcode submit region end(Prohibit modification and deletion)
