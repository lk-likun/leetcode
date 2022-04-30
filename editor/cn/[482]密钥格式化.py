# leetcode submit region begin(Prohibit modification and deletion)
import string


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        a, b = divmod(len(s), k)
        res = list()
        if b:
            res = [s[:b]]
            for i in range(b, len(s), k):
                res.append(s[i:i + k])
        else:
            for i in range(0, len(s), k):
                res.append(s[i:i + k])
        return "-".join(res)


# leetcode submit region end(Prohibit modification and deletion)
#
# S = "5F3Z-2e-9-w"
# k1 = 4
# x = Solution().licenseKeyFormatting(S, k1)
# print(x)
