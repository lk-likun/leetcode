# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        gap = int(n / 2)
        while gap > 0:
            for i in range(gap, n):
                temp = nums[i]
                j = i
                while j >= gap and nums[j - gap] > temp:
                    nums[j] = nums[j - gap]
                    j -= gap
                nums[j] = temp
            gap = int(gap / 2)
        return nums


# leetcode submit region end(Prohibit modification and deletion)

n = [5, 2, 3, 1]
Solution().sortArray(n)
