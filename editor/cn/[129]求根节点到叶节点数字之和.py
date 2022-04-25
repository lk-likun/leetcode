# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, value):
            if not root:
                return 0
            value = value * 10 + root.val
            if not root.left and not root.right:
                return value
            return dfs(root.left, value) + dfs(root.right, value)

        return dfs(root, 0)

# leetcode submit region end(Prohibit modification and deletion)
