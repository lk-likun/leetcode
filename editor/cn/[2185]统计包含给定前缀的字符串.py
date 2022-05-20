# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for i in words:
            res += i.startswith(pref)
        return res
# leetcode submit region end(Prohibit modification and deletion)

