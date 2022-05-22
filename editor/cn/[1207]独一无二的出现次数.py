# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        return len(set(count.values())) == len(count.values())


# leetcode submit region end(Prohibit modification and deletion)

arr1 = [1, 2, 2, 1, 1, 3]
x = Solution().uniqueOccurrences(arr1)
print(x)