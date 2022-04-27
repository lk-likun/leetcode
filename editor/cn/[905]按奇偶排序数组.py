# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = list()
        odd = list()
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even + odd
# leetcode submit region end(Prohibit modification and deletion)
