# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        vals = [[i, nums[i]] for i in range(n)]
        vals.sort(key=lambda x: -x[1])
        vals = sorted(vals[:k])
        res = [val for idx, val in vals]
        return res
# leetcode submit region end(Prohibit modification and deletion)
