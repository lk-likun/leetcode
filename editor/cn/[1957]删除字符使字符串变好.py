# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def makeFancyString(self, s: str) -> str:
        res = list()
        for i in s:
            if len(res) >= 2 and res[-1] == res[-2] == i:
                continue
            res.append(i)
        return "".join(res)


# leetcode submit region end(Prohibit modification and deletion)

s1 = "aaaaaabbbbaaaaaaccccd"
x = Solution().makeFancyString(s1)
print(x)
