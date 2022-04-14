# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

import numpy as np


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))
        # ls = list()
        # for i in accounts:
        #     ls.append(sum(i))
        # return max(ls)
        # return np.max(np.sum(np.array(accounts), axis=1), axis=0)

# leetcode submit region end(Prohibit modification and deletion)
