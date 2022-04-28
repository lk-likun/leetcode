# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for i in counter:
            if counter[i] == 1:
                return i
# leetcode submit region end(Prohibit modification and deletion)
