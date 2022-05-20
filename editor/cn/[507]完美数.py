# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        sum = 1
        d = 2
        while d * d <= num:
            if num % d == 0:
                sum += d
                if d * d < num:
                    sum += num / d
            d += 1
        return sum == num


# leetcode submit region end(Prohibit modification and deletion)
n = 28
Solution().checkPerfectNumber(n)
