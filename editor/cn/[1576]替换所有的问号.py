# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def modifyString(self, s: str) -> str:
        s = list("?" + s + "?")
        for i in range(1, len(s) - 1):
            if s[i] == "?":
                for j in range(97, 123):
                    if chr(j) != s[i + 1] and chr(j) != s[i - 1]:
                        s[i] = chr(j)
                        break
        return "".join(s[1:-1])


# leetcode submit region end(Prohibit modification and deletion)

s1 = "ubv?w"
Solution().modifyString(s1)
