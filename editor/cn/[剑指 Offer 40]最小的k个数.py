# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]
# leetcode submit region end(Prohibit modification and deletion)
