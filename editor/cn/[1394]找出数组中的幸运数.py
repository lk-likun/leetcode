# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        for i in arr:
            if arr.count(i) == i and i > res:
                res = i
        return res

# leetcode submit region end(Prohibit modification and deletion)
