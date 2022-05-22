# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        tmp = ListNode(0, head)
        length = getLength(head)
        cur = tmp
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return tmp.next

# leetcode submit region end(Prohibit modification and deletion)
