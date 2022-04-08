# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         left = 0
#         right = len(nums) - 1
#         if nums[left] >= target:
#             return left
#         if nums[right] < target:
#             return right + 1
#         if nums[right] == target:
#             return right
#         while left + 1 < right:
#             tmp = (left + right) // 2
#             if nums[tmp] > target:
#                 right = tmp
#             elif nums[tmp] < target:
#                 left = tmp
#             else:
#                 return tmp
#         return right

# leetcode submit region end(Prohibit modification and deletion)
