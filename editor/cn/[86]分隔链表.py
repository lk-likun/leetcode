# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        left, right = [], []
        cur = head
        while cur:
            if cur.val < x:
                left.append(cur)
            else:
                right.append(cur)
            cur = cur.next
        ans = left + right + [None]
        for i in range(len(ans) - 1):
            ans[i].next = ans[i + 1]
        return ans[0]
# leetcode submit region end(Prohibit modification and deletion)
