# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic = dict()
        res = -1
        for i in range(len(s)):
            if s[i] not in dic:
                dic.update({s[i]: i})
            else:
                if i - dic[s[i]] - 1 > res:
                    res = i - dic[s[i]] - 1
        return res


# leetcode submit region end(Prohibit modification and deletion)

s1 = "abca"
x = Solution().maxLengthBetweenEqualCharacters(s1)
print(x)