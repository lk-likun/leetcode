# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = list()
        for i in s.lower():
            if i.isalnum():
                ls.append(i)
        return ls == ls[::-1]


# leetcode submit region end(Prohibit modification and deletion)

s1 = "A man, a plan, a canal: Panama"
Solution().isPalindrome(s1)
