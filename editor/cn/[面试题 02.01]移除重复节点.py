# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if head:
            ls = [head.val]
            pre = head
            while pre.next:
                cur = pre.next
                if cur.val not in ls:
                    ls.append(cur.val)
                    pre = pre.next
                else:
                    pre.next = pre.next.next
        return head

# leetcode submit region end(Prohibit modification and deletion)
