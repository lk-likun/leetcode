# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ls = [str(i) for i in nums]
        res = list()
        for i in range(1, len(ls) + 1):
            num = "".join(ls[:i])
            if int(num, 2) % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res


# class Solution:
#     def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
#         ans = []
#         c = 0
#         for i in range(len(nums)):
#             c =  c* 2 + nums[i]
#             c = c % 5
#             ans.append(c == 0)
#         return ans
# leetcode submit region end(Prohibit modification and deletion)

nums1 = [0, 1, 1]
Solution().prefixesDivBy5(nums1)
