# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def compressString(self, S: str) -> str:
        i, j, ls = 0, 0, len(S)
        res = []
        while i < ls:
            while j < ls and S[i] == S[j]:
                j += 1
            res.append(S[i])
            res.append(str(j - i))
            i = j
        res = ''.join(res)
        return res if len(res) < ls else S


# leetcode submit region end(Prohibit modification and deletion)


s = "aabcccccaaa"
Solution().compressString(s)
