# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.right:
            if root.val != root.right.val or not self.isUnivalTree(root.right):
                return False
        if root.left:
            if root.val != root.left.val or not self.isUnivalTree(root.left):
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
