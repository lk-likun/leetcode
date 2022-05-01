# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = list()
        for i in range(0, len(s), k):
            res.append(s[i:i + k])
        tmp = k - len(res[-1])
        if tmp:
            res[-1] += tmp * fill
        return res


# leetcode submit region end(Prohibit modification and deletion)

# s1 = "abcdefghi1"
# k1 = 3
# fill1 = "x"
# Solution().divideString(s1, k1, fill1)
