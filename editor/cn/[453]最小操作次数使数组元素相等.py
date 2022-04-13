# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)

# leetcode submit region end(Prohibit modification and deletion)
