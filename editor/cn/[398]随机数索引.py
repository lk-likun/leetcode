# leetcode submit region begin(Prohibit modification and deletion)
from random import choice
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        ls = list()
        for i, num in enumerate(self.nums):
            if target == num:
                ls.append(i)
        return choice(ls)

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# leetcode submit region end(Prohibit modification and deletion)
