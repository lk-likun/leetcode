# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        ls = list()
        for i in s:
            #     try:
            #         ls.remove(i)
            #     except ValueError:
            #         ls.append(i)
            # return len(ls) < 2
            if i not in ls:
                ls.append(i)
            else:
                ls.remove(i)
        return len(ls) < 2

# leetcode submit region end(Prohibit modification and deletion)
