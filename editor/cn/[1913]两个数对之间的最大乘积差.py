# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        res = sorted(nums)
        return res[-1] * res[-2] - res[0] * res[1]

# leetcode submit region end(Prohibit modification and deletion)
