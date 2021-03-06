# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    @staticmethod
    def removeElement(nums: List[int], val: int) -> int:
        a = 0
        b = 0

        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1

        return b

# leetcode submit region end(Prohibit modification and deletion)
