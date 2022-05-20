# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        ls = list()
        cur = head
        while cur:
            ls.append(cur.val)
            cur = cur.next
        n = len(ls)
        res = ls[n - k % n:] + ls[:n - k % n]
        ans_head = ListNode(res[0])
        cur = ans_head
        for i in range(1, n):
            node = ListNode(res[i])
            cur.next = node
            cur = node
        return ans_head

# leetcode submit region end(Prohibit modification and deletion)
