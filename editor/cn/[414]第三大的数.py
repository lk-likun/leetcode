# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        try:
            return list(sorted(set(nums)))[-3]
        except IndexError:
            return max(nums)
        # if len(set(nums)) >= 3:
        #     return sorted(set(nums))[-3]
        # return max(nums)

# leetcode submit region end(Prohibit modification and deletion)
