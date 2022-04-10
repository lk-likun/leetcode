# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # if n == 0:
        #     return 1
        # elif n == 1:
        #     return 10
        # elif n == 2:
        #     return 91
        # elif n == 3:
        #     return 739
        # elif n == 4:
        #     return 5275
        # elif n == 5:
        #     return 32491
        # elif n == 6:
        #     return 168571
        # elif n == 7:
        #     return 712891
        # else:
        #     return 2345851
        # if n == 0:
        #     return 1

        # if n == 8:
        #     return 2345851
        # tmp = 0
        # for num in range(10 ** n):
        #     if len(set(str(num))) == len(str(num)):
        #         tmp += 1
        # return tmp
        # if n == 0:
        #     return 1
        # return int(9 * (math.factorial(9) / math.factorial(10-n))) + self.countNumbersWithUniqueDigits(n - 1)
        if n == 0:
            return 1
        tmp = 9
        for i in range(n - 1):
            tmp *= (9 - i)
        return tmp + self.countNumbersWithUniqueDigits(n - 1)

# leetcode submit region end(Prohibit modification and deletion)
