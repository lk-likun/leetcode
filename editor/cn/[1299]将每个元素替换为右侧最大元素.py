# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * (n - 1) + [-1]
        for i in range(n - 2, -1, -1):
            res[i] = max(res[i + 1], arr[i + 1])
        return res


# leetcode submit region end(Prohibit modification and deletion)

arr1 = [17, 18, 5, 4, 6, 1]
Solution().replaceElements(arr1)
