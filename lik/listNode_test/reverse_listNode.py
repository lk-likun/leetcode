import multiprocessing


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    ins = None
    node = ListNode()

    def __new__(cls, *args, **kwargs):
        with multiprocessing.RLock():
            if cls.ins is None:
                cls.ins = super().__new__(cls)
            return cls.ins

    def arrayToListNode(self, nums):
        ans_head = self.node
        cur = ans_head
        for i in nums:
            node = ListNode(i)
            cur.next = node
            cur = cur.next
        self.node = ans_head.next

    def reverseListNode(self):
        pre = None
        cur = self.node
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        self.node = pre

    def listNodeToArray(self):
        res = []
        cur = self.node
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res


nums1 = [1, 2, 3, 4, 5]
Solution().arrayToListNode(nums1)
Solution().reverseListNode()
z = Solution().listNodeToArray()
print(z)