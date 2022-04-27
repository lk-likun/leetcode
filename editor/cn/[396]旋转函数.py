# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # c = 0
        # res = list()
        # while c < len(nums):
        #     c += 1
        #     tmp = 0
        #     for i, num in enumerate(nums[c - 1:] + nums[0:c - 1]):
        #         tmp += i*num
        #     res.append(tmp)
        #     # print(res)
        # return max(res)
        res = 0
        tmp = 0
        s = sum(nums)
        n = len(nums)
        s0 = 0
        for i, v in enumerate(nums):
            s0 += i*v
            tmp += s - n * nums[n - 1 - i]
            res = max(res, tmp)
        return max(s0, s0 + res)


# leetcode submit region end(Prohibit modification and deletion)


ls = [4, 3, 2, 6]
x = Solution().maxRotateFunction(ls)
print(x)

