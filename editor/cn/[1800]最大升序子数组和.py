# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        tmp = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                tmp += nums[i]
            else:
                if tmp > res:
                    res = tmp
                tmp = nums[i]
        if tmp > res:
            res = tmp
        return res


# leetcode submit region end(Prohibit modification and deletion)
n = [10, 20, 30, 5, 10, 50]
Solution().maxAscendingSum(n)
