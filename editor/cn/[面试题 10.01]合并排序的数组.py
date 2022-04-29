# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        A[m:] = B
        A.sort()
# leetcode submit region end(Prohibit modification and deletion)

