# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        n = 0
        a = ""
        for c in s:
            if c.isdigit():
                a = a * int(c)
                n *= int(c)
            else:
                a += c
                n += 1
            if n >= k:
                return a[k - 1]


# leetcode submit region end(Prohibit modification and deletion)

S = "leet2code3"
K = 10
x = Solution().decodeAtIndex(S, K)
print(x)