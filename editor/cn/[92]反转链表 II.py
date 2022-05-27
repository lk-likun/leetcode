# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return head
        ls = []
        cur = head
        while cur:
            ls.append(cur.val)
            cur = cur.next
        res = ls[:left - 1] + ls[left - 1:right] + ls[right:]
        ans_head = ListNode(res[0])
        cur = ans_head
        for i in range(1, len(res)):
            node = ListNode(res[i])
            cur.next = node
            cur = node
        return ans_head

# leetcode submit region end(Prohibit modification and deletion)
