# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        if n % 2 == 0:
            mid = (nums1[int(n / 2 - 1)] + nums1[int(n / 2)]) / 2
        else:
            mid = nums1[int((n + 1) / 2 - 1)]
        return mid


# leetcode submit region end(Prohibit modification and deletion)


n1 = [1, 3]
n2 = [2]
x = Solution().findMedianSortedArrays(n1, n2)
print(x)
