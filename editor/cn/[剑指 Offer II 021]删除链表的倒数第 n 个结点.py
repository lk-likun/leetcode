# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # left = right = head
        # i = 0
        # while i < n:
        #     right = right.next
        #     i += 1
        # if not right:
        #     return head.next
        # while right.next:
        #     left = left.next
        #     right = right.next
        # left.next = left.next.next
        # return head
        def getLength(head):
            length = 0
            while head:
                head = head.next
                length += 1
            return length

        dummy_node = ListNode(0, head)
        cur = dummy_node
        length = getLength(head)
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy_node.next
# leetcode submit region end(Prohibit modification and deletion)
