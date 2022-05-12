# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for i in list(zip(*strs)):
            j = 1
            while j < len(i):
                if i[j] < i[j - 1]:
                    res += 1
                    break
                j += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)

s = ["cba", "daf", "ghi"]
x = Solution().minDeletionSize(s)
print(x)
