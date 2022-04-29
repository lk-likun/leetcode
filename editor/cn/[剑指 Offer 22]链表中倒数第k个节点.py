# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        tmp = head
        for i in range(k):
            tmp = tmp.next
        while tmp:
            tmp, head = tmp.next, head.next
        return head

# leetcode submit region end(Prohibit modification and deletion)
