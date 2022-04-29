# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        res = 0
        for i in range(1, n + 1):
            mid = n / i
            step = (i - 1) / 2
            low = mid - step
            print(i, mid, low)
            if low < 1:
                break
            if low % 1 == 0:
                res += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)


Solution().consecutiveNumbersSum(100)