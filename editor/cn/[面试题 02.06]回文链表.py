# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ls = list()
        tmp = head
        while tmp:
            ls.append(tmp.val)
            tmp = tmp.next
        return ls == ls[::-1]
# leetcode submit region end(Prohibit modification and deletion)
