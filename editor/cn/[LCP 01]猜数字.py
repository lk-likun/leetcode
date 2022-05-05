# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        res = 0
        for i in zip(guess, answer):
            res += i[0] == i[1]
        return res


# leetcode submit region end(Prohibit modification and deletion)
g = [1, 2, 3]
a = [1, 1, 1]
Solution().game(g, a)
