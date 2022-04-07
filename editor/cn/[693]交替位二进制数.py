# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    @staticmethod
    def hasAlternatingBits(n: int) -> bool:
        x = n ^ (n >> 1)
        return math.log2(x + 1) % 1 == 0
# leetcode submit region end(Prohibit modification and deletion)
