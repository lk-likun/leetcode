# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = list()
        for i in range(len(nums)):
            res.insert(index[i], nums[i])
        return res


# leetcode submit region end(Prohibit modification and deletion)

nums1 = [0, 1, 2, 3, 4]
index1 = [0, 1, 2, 2, 1]
x = Solution().createTargetArray(nums1, index1)
print(x)
