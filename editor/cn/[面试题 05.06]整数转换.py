# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        return bin((A & 0xffffffff) ^ (B & 0xffffffff)).count('1')


# leetcode submit region end(Prohibit modification and deletion)

a = 29
b = 15
x = Solution().convertInteger(a, b)
print(x)