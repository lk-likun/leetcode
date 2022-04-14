# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # res = 0
        # for i in nums:
        #     if i == target:
        #         res += 1
        # return res
        return nums.count(target)
# leetcode submit region end(Prohibit modification and deletion)

