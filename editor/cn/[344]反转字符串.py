# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def reverseString(self, s: List[str]):
        """
        Do not return anything, modify s in-place instead.
        """
        right = len(s)
        for i in range(right // 2):
            s[i], s[right - i - 1] = s[right - i - 1], s[i]

# leetcode submit region end(Prohibit modification and deletion)