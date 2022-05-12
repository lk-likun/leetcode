# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= start + i * 2
        return res

# leetcode submit region end(Prohibit modification and deletion)
