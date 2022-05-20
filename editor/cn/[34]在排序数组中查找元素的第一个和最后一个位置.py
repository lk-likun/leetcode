# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        ans = [0, 0]
        left = -1
        right = len(nums)
        while left != right - 1:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        ans[0] = right
        left = -1
        right = len(nums)
        while left != right - 1:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        ans[1] = left
        return ans


# leetcode submit region end(Prohibit modification and deletion)


nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
x = Solution().searchRange(nums1, target1)
print(x)
