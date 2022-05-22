# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        head1 = head.next
        head.next = self.swapPairs(head1.next)
        head1.next = head
        return head1
# leetcode submit region end(Prohibit modification and deletion)
