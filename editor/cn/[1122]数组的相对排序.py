# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = dict()
        ls = list()
        for a in arr1:
            if a in arr2:
                ai = arr2.index(a)
                tmp = d.get(ai, list())
                tmp += [a]
                d.update({ai: tmp})
            else:
                ls.append(a)
        ls.sort()
        res = list()
        for i in range(len(arr2)):
            res += d.get(i)
        res += ls
        return res
# leetcode submit region end(Prohibit modification and deletion)
