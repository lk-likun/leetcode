# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        x, cnt = -1, 0
        for i in nums:
            if not cnt:
                x = i
            if x == i:
                cnt += 1
            else:
                cnt -= 1
        return x if cnt and nums.count(x) > n // 2 else -1

# leetcode submit region end(Prohibit modification and deletion)
