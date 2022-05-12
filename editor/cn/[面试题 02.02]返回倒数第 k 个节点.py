# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        pre = head
        cur = head
        for i in range(k):
            cur = cur.next
        while cur:
            pre = pre.next
            cur = cur.next
        return pre.val
# leetcode submit region end(Prohibit modification and deletion)
