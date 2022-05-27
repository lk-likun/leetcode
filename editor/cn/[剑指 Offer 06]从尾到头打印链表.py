# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = list()
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res[::-1]

# leetcode submit region end(Prohibit modification and deletion)
