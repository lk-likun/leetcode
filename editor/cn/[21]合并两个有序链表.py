# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# leetcode submit region end(Prohibit modification and deletion)

# def gen_list(ls):
#     if not ls:
#         return None
#     return ListNode(val=ls[0], next=gen_list(ls[1:]))


# x = ListNode(val=10)
# A = ListNode(val=5, next=x)
# B = ListNode(val=3, next=ListNode(val=8))
# f = Solution()
# f.mergeTwoLists(A, B)
# ls0 = [3, 6, 9, 15, 20]
# n = gen_list(ls0)
