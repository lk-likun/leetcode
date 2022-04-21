# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
# leetcode submit region end(Prohibit modification and deletion)

