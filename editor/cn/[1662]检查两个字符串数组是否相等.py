# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
# leetcode submit region end(Prohibit modification and deletion)
