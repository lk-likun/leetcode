# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # if len(set(nums)) == 1:
        #     return 0
        # s = sum(nums)
        # t = s // len(nums) + 1
        # while True:
        #     a = t * len(nums) - s
        #     b = len(nums) - 1
        #     print(a, b, t)
        #     if a % b == 0 and :
        #         return int(a / b)
        #     t += 1
        return sum(nums) - min(nums) * len(nums)

# leetcode submit region end(Prohibit modification and deletion)
# ls = [1, 1000000000]
# x = Solution().minMoves(ls)
# print(x)
