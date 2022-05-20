# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n == len(original):
            res = []
            for i in range(0, len(original), n):
                res.append(original[i: i + n])
            return res
        else:
            return []
# leetcode submit region end(Prohibit modification and deletion)
