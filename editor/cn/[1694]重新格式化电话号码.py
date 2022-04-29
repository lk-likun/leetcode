# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '').replace('-', '')
        i = 0
        ls = list()
        while i < len(number):
            ls.append(number[i: i+3])
            i += 3
        if len(ls[-1]) == 1:
            ls[-1] = ls[-2][-1] + ls[-1]
            ls[-2] = ls[-2][:-1]
        return '-'.join(ls)

# leetcode submit region end(Prohibit modification and deletion)

