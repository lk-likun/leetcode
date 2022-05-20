# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

import numpy as np


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        mid = nums[n // 2]
        ans = 0
        for i in nums:
            ans += abs(mid - i)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


# nums1 = [1, 2, 3]
nums1 = [1, 10, 2, 9]
x = Solution().minMoves2(nums1)
print(x)
