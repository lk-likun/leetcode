# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if i == i[::-1]:
                return i
        return ''
# leetcode submit region end(Prohibit modification and deletion)
