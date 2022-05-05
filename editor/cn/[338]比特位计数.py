# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(i).count("1") for i in range(n + 1)]


# leetcode submit region end(Prohibit modification and deletion)

n1 = 5
Solution().countBits(n1)
