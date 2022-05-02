# leetcode submit region begin(Prohibit modification and deletion)
import string


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        global res
        dic = dict(zip(string.ascii_lowercase, [i + 1 for i in range(27)]))
        init_num = ""
        for i in s:
            init_num += str(dic[i])
        while k > 0:
            res = 0
            for i in init_num:
                res += int(i)
            init_num = str(res)
            k -= 1
        return res


# leetcode submit region end(Prohibit modification and deletion)

s1 = "leetcode"
k1 = 2
x = Solution().getLucky(s1, k1)
print(x)
