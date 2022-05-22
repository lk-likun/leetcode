# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        ls1 = set()
        ls2 = list()
        cur = head
        while cur:
            if cur.val not in ls1 and cur.val not in ls2:
                ls1.add(cur.val)
                ls2.append(cur.val)
            elif cur.val in ls1 and cur.val in ls2:
                ls2.remove(cur.val)
            cur = cur.next
        if not ls2:
            return None
        ans_head = ListNode(ls2[0])
        cur = ans_head
        for i in range(1, len(ls2)):
            node = ListNode(ls2[i])
            cur.next = node
            cur = node
        return ans_head

# leetcode submit region end(Prohibit modification and deletion)
