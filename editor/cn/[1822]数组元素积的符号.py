# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                res *= -1
        return res


# leetcode submit region end(Prohibit modification and deletion)
