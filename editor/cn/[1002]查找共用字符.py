# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        tmp = collections.Counter(words[0])
        ans = []
        for i in range(1, len(words)):
            tmp = tmp & collections.Counter(words[i])
        for j in tmp:
            v = tmp[j]
            while v:
                ans.append(j)
                v -= 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)

words1 = ["bella", "label", "roller"]
x = Solution().commonChars(words1)
print(x)
