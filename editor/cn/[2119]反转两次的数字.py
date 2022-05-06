# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # if num == 0:
        #     return True
        # return str(num)[-1] != "0"
        return num == 0 or num % 10 != 0
# leetcode submit region end(Prohibit modification and deletion)
