# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if val == root.val:
            return root
        return self.searchBST(root.left if val < root.val else root.right, val)


# leetcode submit region end(Prohibit modification and deletion)
