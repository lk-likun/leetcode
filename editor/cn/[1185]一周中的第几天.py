# leetcode submit region begin(Prohibit modification and deletion)
import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime.datetime(year, month, day).strftime("%A")


# leetcode submit region end(Prohibit modification and deletion)
d = 31
m = 8
y = 2019
Solution().dayOfTheWeek(d, m, y)
