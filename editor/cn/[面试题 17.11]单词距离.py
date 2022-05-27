# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        n = len(words)
        index1, index2 = -1, -1
        for i, v in enumerate(words):
            if v == word1:
                index1 = i
            elif v == word2:
                index2 = i
            if index1 >= 0 and index2 >= 0:
                n = min(n, abs(index2 - index1))
        return n


# leetcode submit region end(Prohibit modification and deletion)

words_ = ["I", "am", "a", "student", "from", "a", "university", "in", "a", "city"]
word1_ = "a"
word2_ = "student"

x = Solution().findClosest(words_, word1_, word2_)
print(x)