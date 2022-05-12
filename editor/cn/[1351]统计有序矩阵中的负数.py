# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for i in grid:
            for j in i:
                if j < 0:
                    res += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)

