# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    if i * j % k == 0:
                        res += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)

nums1 = [3, 1, 2, 2, 2, 1, 3]
k1 = 2
x = Solution().countPairs(nums1, k1)
print(x)