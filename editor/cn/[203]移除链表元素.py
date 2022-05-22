# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        else:
            head.next = self.removeElements(head.next, val)
            return head.next if head.val == val else head

# leetcode submit region end(Prohibit modification and deletion)
