# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum_nums = 0
        for i, v in collections.Counter(nums).items():
            if v == 1:
                sum_nums += i
        return sum_nums


# leetcode submit region end(Prohibit modification and deletion)


n = [1, 2, 3, 2]
Solution().sumOfUnique(n)
