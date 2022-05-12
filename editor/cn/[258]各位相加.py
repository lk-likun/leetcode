# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            sumNum = 0
            while num:
                sumNum += num % 10
                num //= 10
            num = sumNum
        return num


# leetcode submit region end(Prohibit modification and deletion)

n = 382
x = Solution().addDigits(n)
print(x)