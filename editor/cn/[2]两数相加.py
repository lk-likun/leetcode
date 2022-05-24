# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ls1, ls2 = [], []
        while l1:
            ls1.append(l1.val)
            l1 = l1.next
        while l2:
            ls2.append(l2.val)
            l2 = l2.next
        sumNum = int(''.join([str(i) for i in ls1])) + int(''.join([str(i) for i in ls2]))
        ls_sum = [int(i) for i in str(int(str(sumNum)[::-1]))][::-1]
        ans_head = ListNode()
        cur = ans_head
        for i in ls_sum:
            node = ListNode(i)
            cur.next = node
            cur = cur.next
        return ans_head.next
    # leetcode submit region end(Prohibit modification and deletion)
