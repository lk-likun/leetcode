# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = list()
        tmp1 = 0
        tmp2 = len(s)
        for i in s:
            if i == "I":
                res.append(tmp1)
                tmp1 += 1
            else:
                res.append(tmp2)
                tmp2 -= 1
        res.append(tmp1)
        return res


# leetcode submit region end(Prohibit modification and deletion)

s1 = "IDID"
x = Solution().diStringMatch(s1)
print(x)
