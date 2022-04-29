# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def pow_sum(self, n):
        n1, n2 = divmod(n, 10)
        if n1 == 0:
            return pow(n2, 2)
        return pow(n2, 2) + self.pow_sum(n1)

    def isHappy(self, n: int) -> bool:
        ls = list()
        while True:
            n = self.pow_sum(n)
            if n == 1:
                return True
            if n in ls:
                return False
            ls.append(n)

# leetcode submit region end(Prohibit modification and deletion)