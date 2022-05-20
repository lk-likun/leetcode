# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res = []
        tmp = head
        while tmp:
            res.append(tmp.val)
            tmp = tmp.next
        return res == res[::-1]

# leetcode submit region end(Prohibit modification and deletion)
