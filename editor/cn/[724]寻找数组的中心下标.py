# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     if sum(nums[:i]) == sum(nums[i + 1:]):
        #         return i
        # return -1

        n = len(nums)
        sum0, sum1 = sum(nums), 0
        for i in range(n):
            if sum1 * 2 + nums[i] == sum0:
                return i
            sum1 += nums[i]
        return -1


# leetcode submit region end(Prohibit modification and deletion)

nums1 = [1, 7, 3, 6, 5, 6]
x = Solution().pivotIndex(nums1)
print(x)
