# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        s = sorted(nums)
        return s == nums or s == nums[::-1]

# leetcode submit region end(Prohibit modification and deletion)
