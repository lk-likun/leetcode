# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = list(s)
        for i in range(0, len(s), k*2):
            res[i:i+k] = reversed(res[i:i+k])
        return ''.join(res)


# leetcode submit region end(Prohibit modification and deletion)

s1 = "abcdefg"
k1 = 2
x = Solution().reverseStr(s1, k1)
print(x)