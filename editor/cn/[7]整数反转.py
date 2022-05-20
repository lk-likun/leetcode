# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            s = str(x)[:0:-1]
            return 0 - int(s) if 0 - int(s) >= -2 ** 31 else 0
        else:
            s = str(x)[::-1]
            return int(s) if int(s) < 2 ** 31 - 1 else 0


# leetcode submit region end(Prohibit modification and deletion)

x1 = 120
x = Solution().reverse(x1)
print(x)
