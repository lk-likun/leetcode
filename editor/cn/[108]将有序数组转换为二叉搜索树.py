# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.traversal(nums, 0, len(nums) - 1)

    def traversal(self, nums, left, right):
        if right < left:
            return None
        mid = (right + left) // 2
        mid_root = TreeNode(nums[mid])
        mid_root.left = self.traversal(nums, left, mid - 1)
        mid_root.right = self.traversal(nums, mid + 1, right)
        return mid_root


# leetcode submit region end(Prohibit modification and deletion)

nums1 = [-10, -3, 0, 5, 9]
x = Solution().sortedArrayToBST(nums1)
print(x.right.left.val)
