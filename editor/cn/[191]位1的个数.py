# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    def hammingWeight(self, n: int) -> int:
        # res = 0
        # for i in bin(n)[2:]:
        #     if i == "1":
        #         res += 1
        # return res
        # 数学
        # if n == 0:
        #     return n
        # return 1 + self.hammingWeight(int(n - math.pow(2, int(math.log2(n)))))
        return bin(n).count("1")
# leetcode submit region end(Prohibit modification and deletion)
