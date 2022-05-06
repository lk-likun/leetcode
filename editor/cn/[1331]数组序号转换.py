# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ls = sorted(set(arr))
        dic = dict()
        for i, v in enumerate(ls):
            dic[v] = i + 1
        for i in range(len(arr)):
            arr[i] = dic[arr[i]]
        return arr


# leetcode submit region end(Prohibit modification and deletion)

arr1 = [37, 12, 28, 9, 100, 56, 80, 5, 12]
Solution().arrayRankTransform(arr1)
