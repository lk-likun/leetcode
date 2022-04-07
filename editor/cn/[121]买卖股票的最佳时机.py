# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        res = 0
        min_p = prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] - min_p)
            min_p = min(min_p, prices[i])
        return res
# leetcode submit region end(Prohibit modification and deletion)
