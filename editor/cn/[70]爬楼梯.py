# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     @staticmethod
#     def climbStairs(n: int) -> int:
#         if n <= 2:
#             return n
#         else:
#             return Solution.climbStairs(n - 1) + Solution.climbStairs(n - 2)
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        # 遍历背包
        for i in range(2, n + 1):
            # 遍历物品
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

# leetcode submit region end(Prohibit modification and deletion)
