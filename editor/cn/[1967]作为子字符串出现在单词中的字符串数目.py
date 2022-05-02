# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        for i in patterns:
            if i in word:
                res += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
