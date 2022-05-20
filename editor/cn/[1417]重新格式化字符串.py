# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reformat(self, s: str) -> str:
        letters = list()
        nums = list()
        for i in s:
            if i.isalpha():
                letters.append(i)
            else:
                nums.append(i)
        res = list()
        if abs(len(letters) - len(nums)) > 1:
            return ""
        if len(letters) == len(nums):
            for i in zip(letters, nums):
                res += i
            return "".join(res)
        elif len(letters) > len(nums):
            for i in zip(letters, nums):
                res += i
            return "".join(res) + letters[-1]
        else:
            for i in zip(nums, letters):
                res += i
            return "".join(res) + nums[-1]


# leetcode submit region end(Prohibit modification and deletion)
s1 = "covid2019"
Solution().reformat(s1)
