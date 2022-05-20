# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = list()
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        return res
# leetcode submit region end(Prohibit modification and deletion)

