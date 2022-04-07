# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = str()
        for i in zip(*strs):
            if len(set(i)) != 1:
                break
            res += list(set(i))[0]
        return res

# leetcode submit region end(Prohibit modification and deletion)
