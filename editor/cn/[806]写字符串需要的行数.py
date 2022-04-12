# leetcode submit region begin(Prohibit modification and deletion)
import string
from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        dic = dict(zip(string.ascii_lowercase, widths))
        tmp = 0
        layer = 1
        for i in s:
            if tmp + dic[i] > 100:
                layer += 1
                tmp = dic[i]
                continue
            tmp += dic[i]
        return [layer, tmp]

# leetcode submit region end(Prohibit modification and deletion)
