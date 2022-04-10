# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = list()
        for i in str(int(''.join([str(i) for i in digits])) + 1):
            res.append(int(i))
        return res

# leetcode submit region end(Prohibit modification and deletion)
# ls = [1, 2, 3]
# ls1 = [str(i) for i in ls]
# x = int(''.join(ls1))
# print(x + 1)
# ls2 = list()
# for i in str(x+1):
#     ls2.append(int(i))
# print(ls2)
