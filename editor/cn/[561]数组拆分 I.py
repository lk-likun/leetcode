# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # ls = sorted(nums)
        # res = 0
        # for i in range(len(ls)):
        #     if i % 2 == 0:
        #         res += ls[i]
        # return res
        nums.sort()
        return sum(nums[::2])


# leetcode submit region end(Prohibit modification and deletion)

n1 = [6, 2, 6, 5, 1, 2]
Solution().arrayPairSum(n1)
