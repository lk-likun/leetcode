# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # s = "".join(map(str, nums))
        # return len(max(s.split("0")))
        res = 0
        tmp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                tmp += 1
                continue
            res = max(res, tmp)
            tmp = 0
        res = max(res, tmp)
        return res

# leetcode submit region end(Prohibit modification and deletion)
