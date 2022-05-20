# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [i for i in range(1 - n, n, 2)]


# leetcode submit region end(Prohibit modification and deletion)


n1 = 5
Solution().sumZero(n1)
