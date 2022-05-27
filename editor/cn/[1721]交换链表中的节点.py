# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # ls = []
        # cur = head
        # while cur:
        #     ls.append(cur.val)
        #     cur = cur.next
        # ls[k-1], ls[-k] = ls[-k], ls[k-1]
        # ans = ListNode()
        # cur = ans
        # for i in range(len(ls)):
        #     cur.next = ListNode(ls[i])
        #     cur = cur.next
        # return ans.next
        cur = head
        n1 = head
        n2 = None
        i = 1
        while cur:
            if i == k - 1:
                n1 = cur.next
                n2 = cur.next
            if i >= 2 * k:
                n2 = n2.next
            cur = cur.next
            i += 1
        cur = head
        j = 1
        while i <= 2 * k:
            if j == i - k:
                n2 = cur
                break
            cur = cur.next
            j += 1
        n1.val, n2.val = n2.val, n1.val
        return head


# leetcode submit region end(Prohibit modification and deletion)

ls = [100, 90]
kt = 2
nod = ListNode()
c = nod
for z in ls:
    c.next = ListNode(z)
    c = c.next

x = Solution().swapNodes(nod.next, kt)
while x:
    print(x.val, end=', ')
    x = x.next
