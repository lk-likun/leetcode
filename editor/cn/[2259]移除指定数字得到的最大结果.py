# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeDigit(self, s: str, digit: str) -> str:
        return max(s[:i] + s[i + 1:] for i, v in enumerate(s) if v == digit)


# leetcode submit region end(Prohibit modification and deletion)

number1 = "123"
digit1 = "3"
x = Solution().removeDigit(number1, digit1)
print(x)
