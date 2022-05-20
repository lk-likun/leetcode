# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # res = len(words)
        # for word in words:
        #     for i in set(word):
        #         if i not in allowed:
        #             res -= 1
        #             break
        # return res

        result = 0
        for word in words:
            if word.strip(allowed) == '':
                result += 1
        return result
# leetcode submit region end(Prohibit modification and deletion)
