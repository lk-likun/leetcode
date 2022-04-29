# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, max(nums) - min(nums) - 2 * k)

# leetcode submit region end(Prohibit modification and deletion)
