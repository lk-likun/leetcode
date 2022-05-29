# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = []
        self.getPaths(root, '', res)
        nums = [int(i, 2) for i in res]
        return sum(nums)

    def getPaths(self, root, path, res):
        if not root:
            return
        path += str(root.val)
        if not root.left and not root.right:
            res.append(path)
        else:
            self.getPaths(root.left, path, res)
            self.getPaths(root.right, path, res)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    b = '100'
    t = int(b, 2)
    print(t)
