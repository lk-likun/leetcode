# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return pow(a, int("".join(map(str, b))), 1337)

# leetcode submit region end(Prohibit modification and deletion)
