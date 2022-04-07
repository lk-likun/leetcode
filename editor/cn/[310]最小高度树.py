# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        pass


# leetcode submit region end(Prohibit modification and deletion)

n = 4
edges = [[1, 0], [1, 2], [1, 3]]
dic = collections.defaultdict(list)
print(dic)
for x, y in edges:
    dic[x].append(y)
    dic[y].append(x)
print(dic)
