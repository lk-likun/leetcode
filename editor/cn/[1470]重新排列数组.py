# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int):
        res = []
        for i in zip(nums[0:n], nums[n:2 * n]):
            res += i
        return list(res)


# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         nums[::2], nums[1::2] = nums[:n], nums[n:]
#         return nums


# leetcode submit region end(Prohibit modification and deletion)
ls = [2, 5, 1, 3, 4, 7]
l = 3
Solution().shuffle(ls, l)
