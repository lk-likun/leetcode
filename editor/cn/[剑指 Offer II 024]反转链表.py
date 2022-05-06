# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(pre, cur):
            if not cur:
                return pre

            tmp = cur.next
            cur.next = pre

            return reverse(cur, tmp)

        return reverse(None, head)
# leetcode submit region end(Prohibit modification and deletion)
