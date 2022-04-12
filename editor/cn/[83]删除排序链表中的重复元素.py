# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode):
        if head is None or head.next is None:
            return head
        tmp = head
        if tmp.val == tmp.next.val:
            tmp.next = tmp.next.next
            return self.deleteDuplicates(tmp)
        else:
            tmp = tmp.next
            head.next = self.deleteDuplicates(tmp)
            return head
        # res = [head]
        # cur = list()
        # node = ListNode()
        # tmp = node
        # while res:
        #     i = res.pop(0)
        #     if i is None:
        #         tmp.next = None
        #         return node.next
        #     if i.val not in cur:
        #         cur.append(i.val)
        #         tmp.next = i
        #         tmp = tmp.next
        #     res.append(i.next)

# leetcode submit region end(Prohibit modification and deletion)
