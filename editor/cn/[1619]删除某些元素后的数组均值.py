# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        nums = sorted(arr)
        n = int(len(nums) * 0.05)
        res = sum(nums[n:0 - n]) / len(nums[n:0 - n])
        return res
# leetcode submit region end(Prohibit modification and deletion)
