# leetcode submit region begin(Prohibit modification and deletion)
import math
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # res = 0
        # x = ''.join(map(str, [0]+flowerbed+[0])).split('1')
        # for i in x:
        #     res += math.ceil(i.count('0')/2)-1
        # return n <= res
        res = 0
        tmp = 0
        flowerbed = [0] + flowerbed + [0, 1]
        for i in flowerbed:
            if i == 1 and tmp:
                res += (tmp - 1) // 2
                tmp = 0
            if i == 0:
                tmp += 1
        return n <= res


# leetcode submit region end(Prohibit modification and deletion)

a = [1, 0, 0, 0, 1]
b = 1
x = Solution().canPlaceFlowers(a, b)
print(x)