# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
# leetcode submit region end(Prohibit modification and deletion)
