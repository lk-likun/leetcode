# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        pre = head
        cur = head.next
        while cur and cur.val != val:
            pre = cur
            cur = cur.next
        pre.next = cur.next
        return head
# leetcode submit region end(Prohibit modification and deletion)
