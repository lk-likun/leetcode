# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = dict(zip(order, range(1, 26)))
        for word in words:
            for i in word:
                pass

//////////////////////////////////////////////////////////////////////
# leetcode submit region end(Prohibit modification and deletion)

# words1 = ["hello", "leetcode"]
# order1 = "hlabcdefgijkmnopqrstuvwxyz"
words1 = ["word", "world", "row"]
order1 = "worldabcefghijkmnpqstuvxyz"
x = Solution().isAlienSorted(words1, order1)
print(x)
