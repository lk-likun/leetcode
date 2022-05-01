# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1 = coordinates[1][0] - coordinates[0][0]
        y1 = coordinates[1][1] - coordinates[0][1]

        for i in range(len(coordinates)):
            x2 = coordinates[i][0] - coordinates[0][0]
            y2 = coordinates[i][1] - coordinates[0][1]
            if x1 * y2 != x2 * y1:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)

arr = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
Solution().checkStraightLine(arr)
