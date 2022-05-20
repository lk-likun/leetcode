# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        ls = sorted(salary)[1:-1]
        return sum(ls) / len(ls)
# leetcode submit region end(Prohibit modification and deletion)

