# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # tmp = str()
        # res = list()
        # for j, i in enumerate(nums):
        #     if not tmp:
        #         tmp += str(i)
        #         if j == len(nums) - 1:
        #             res.append(tmp)
        #         continue
        #     t_s = tmp.split("->")
        #     if int(t_s[-1]) + 1 == i:
        #         tmp = t_s[0] + "->" + str(i)
        #         if j == len(nums) - 1:
        #             res.append(tmp)
        #     else:
        #         res.append(tmp)
        #         tmp = str(i)
        #         if j == len(nums) - 1:
        #             res.append(tmp)
        # return res
        if len(nums) == 1:
            return [str(nums[0])]
        tmp = str(nums[0])
        for i, v in enumerate(nums[1:]):
            if v != nums[0] + i + 1:
                if i != 0:
                    tmp += f'->{nums[i]}'
                return [tmp] + self.summaryRanges(nums[i + 1:])
        tmp += f'->{nums[-1]}'
        return [tmp]


# leetcode submit region end(Prohibit modification and deletion)
nums1 = [0, 1, 2, 4, 5, 7]
x = Solution().summaryRanges(nums1)
print(x)
