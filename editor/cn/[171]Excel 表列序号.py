# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        if not columnTitle:
            return 0
        return 26 * self.titleToNumber(columnTitle[:-1]) + ord(columnTitle[-1]) - 64


# leetcode submit region end(Prohibit modification and deletion)