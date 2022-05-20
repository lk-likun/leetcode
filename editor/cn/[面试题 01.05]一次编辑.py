# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        # low += 'a'
        # up += 'a'
        # f_l = len(low)
        # u_l = len(up)
        # if abs(f_l - u_l) > 1:
        #     return False
        # if f_l == u_l:
        #     k = 0
        #     mark = 0
        #     while k < f_l:
        #         if mark > 1:
        #             return False
        #         if low[k] != up[k]:
        #             mark += 1
        #         k += 1
        #     return True
        # if f_l > u_l:
        #     low, up = up, low
        # low += 'a'
        # i = 0
        # j = 0
        # while i < len(up):
        #     if i - j > 1:
        #         return False
        #     if up[i] == low[j]:
        #         i += 1
        #         j += 1
        #     else:
        #         i += 1
        # return True
        lf = len(first)
        ls = len(second)
        if abs(lf - ls) > 1:
            return False
        if lf > ls:
            first, second = second, first
        for i in range(len(first)):
            if first[i] == second[i]:
                continue
            return first[i:] == second[i + 1:] or first[i + 1:] == second[i + 1:]
        return True


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    a = "teacher"
    b = "taches"
    x = Solution().oneEditAway(a, b)
    print(x)
