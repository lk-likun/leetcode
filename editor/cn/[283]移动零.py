# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[tmp], nums[i] = nums[i], nums[tmp]
                tmp += 1


# leetcode submit region end(Prohibit modification and deletion)

nums1 = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums1)
