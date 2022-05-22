# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = self.toArray(head)
        root = self.traversal(nums, 0, len(nums) - 1)
        return root

    def toArray(self, head: Optional[ListNode]) -> List:
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        return ls

    def traversal(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left > right:
            return None
        mid = left + (right - left) // 2
        mid_root = TreeNode(nums[mid])
        mid_root.left = self.traversal(nums, left, mid - 1)
        mid_root.right = self.traversal(nums, mid + 1, right)
        return mid_root
# leetcode submit region end(Prohibit modification and deletion)
