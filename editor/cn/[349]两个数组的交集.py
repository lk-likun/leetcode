# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


# leetcode submit region end(Prohibit modification and deletion)

n1 = [4, 9, 5]
n2 = [9, 4, 9, 8, 4]
Solution().intersection(n1, n2)
