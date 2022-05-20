# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = list()
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res


# leetcode submit region end(Prohibit modification and deletion)

n1 = 3
x = Solution().fizzBuzz(n1)
print(x)
