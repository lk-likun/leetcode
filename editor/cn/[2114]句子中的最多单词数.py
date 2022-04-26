# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for i in sentences:
            tmp = i.count(" ")
            if tmp > res:
                res = tmp
        return res + 1
# leetcode submit region end(Prohibit modification and deletion)
