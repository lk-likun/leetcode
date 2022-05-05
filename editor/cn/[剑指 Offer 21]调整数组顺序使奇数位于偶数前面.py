# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        ls1 = list()
        ls2 = list()
        for i in nums:
            if i % 2 != 0:
                ls1.append(i)
                continue
            ls2.append(i)
        return ls1 + ls2
# leetcode submit region end(Prohibit modification and deletion)
