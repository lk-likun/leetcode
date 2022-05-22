# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = dict()
        ls = list()
        for i, v in enumerate(s):
            tmp = dic.get(v, 0) + 1
            dic.update({v: tmp})
            if tmp == 1:
                ls.append(v)
            if tmp > 1 and v in ls:
                ls.remove(v)
        if not ls:
            return " "
        return ls[0]


# leetcode submit region end(Prohibit modification and deletion)
s1 = "loveleetcode"
x = Solution().firstUniqChar(s1)
print(x)
