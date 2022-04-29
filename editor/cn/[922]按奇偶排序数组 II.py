# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # even = list()
        # odd = list()
        # for num in nums:
        #     if num % 2 == 0:
        #         even.append(num)
        #     else:
        #         odd.append(num)
        # res = list()
        # for i in zip(even, odd):
        #     res += i
        # return res

        even = list()
        odd = list()
        for i, v in enumerate(nums):
            if i % 2 == 0 and v % 2 != 0:
                even.append(i)
            if i % 2 != 0 and v % 2 == 0:
                odd.append(i)
            if even and odd:
                t_1 = even.pop()
                t_2 = odd.pop()
                nums[t_1], nums[t_2] = nums[t_2], nums[t_1]
        return nums


# leetcode submit region end(Prohibit modification and deletion)
n = [4, 2, 5, 7]
x = Solution().sortArrayByParityII(n)
print(x)
