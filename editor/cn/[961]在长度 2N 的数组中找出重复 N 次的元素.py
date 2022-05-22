# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        for num in nums:
            if nums.count(num) == n // 2:
                return num


# leetcode submit region end(Prohibit modification and deletion)

nums1 = [5, 1, 5, 2, 5, 3, 5, 4]
x = Solution().repeatedNTimes(nums1)
print(x)
