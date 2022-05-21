# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return right


# leetcode submit region end(Prohibit modification and deletion)

nums1 = [1, 3, 6, 3, 1]
x = Solution().findPeakElement(nums1)
print(x)
