# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2))[2:])

# leetcode submit region end(Prohibit modification and deletion)

# a = '11'
# b = '1'
# x = int(a, 2) + int(b, 2)
# print(str(bin(x)[2:]))
