# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseWords(self, s: str) -> str:
        # res = ""
        # for i in s.split(" "):
        #     res += i[::-1] + " "
        # res = res[::-1].replace(" ", "", 1)[::-1]
        # return res
        ls = list()
        for i in s.split(" "):
            ls.append(i[::-1])
        return " ".join(ls)


# leetcode submit region end(Prohibit modification and deletion)

s1 = "Let's take LeetCode contest"
Solution().reverseWords(s1)
