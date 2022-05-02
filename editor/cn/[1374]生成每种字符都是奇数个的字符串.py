# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            return "a" * (n - 1) + "b"
        return "a" * n

# leetcode submit region end(Prohibit modification and deletion)
