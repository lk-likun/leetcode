# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i, v in enumerate(nums):
            if target - v in dic:
                return [i, dic[target - v]]
            dic.update({v: i})

# leetcode submit region end(Prohibit modification and deletion)

