# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur_a, cur_b = headA, headB  # 用两个指针代替a和b

        while cur_a != cur_b:
            cur_a = cur_a.next if cur_a else headB  # 如果a走完了，那么就切换到b走
            cur_b = cur_b.next if cur_b else headA  # 同理，b走完了就切换到a

        return cur_a

# leetcode submit region end(Prohibit modification and deletion)
