# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        # ls1 = list()
        # i = 0
        # i2 = 0
        # res = 0
        # while i < len(s):
        #     if s[i] not in ls1:
        #         ls1.append(s[i])
        #         i += 1
        #         if i == len(s):
        #             if len(ls1) > res:
        #                 res = len(ls1)
        #             ls1 = list()
        #             i2 += 1
        #             i = i2
        #     else:
        #         if len(ls1) > res:
        #             res = len(ls1)
        #         ls1 = list()
        #         i2 += 1
        #         i = i2
        # return res
        # start = 0
        # i = 0
        # res = 0
        # dic = dict()
        # while i < len(s):
        #     if s[i] in dic:
        #         tmp = i - start
        #         if tmp > res:
        #             res = tmp
        #         start = dic.get(s[i]) + 1
        #         i = start
        #         dic = dict()
        #         continue
        #     if i == len(s) - 1:
        #         tmp = i - start + 1
        #         if tmp > res:
        #             res = tmp
        #         return res
        #     dic.update({s[i]: i})
        #     i += 1
        # return res
        start, res,cache = 0,0,{}
        for i, c in enumerate(s):
            if c in cache and cache[c] >= start:
                start = cache[c] + 1
                cache[c] = i
            else:
                cache[c] = i
                cur = i - start + 1
                res = max(res, cur)
        return res


# leetcode submit region end(Prohibit modification and deletion)
s1 = 'dd'
x = Solution().lengthOfLongestSubstring(s1)
print(x)
