# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    @staticmethod
    def rotateString(s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s
# leetcode submit region end(Prohibit modification and deletion)
