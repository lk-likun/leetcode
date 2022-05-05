# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reformatDate(self, date: str) -> str:
        dic = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
               'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
        res = date.split(" ")
        res[0] = res[0][:-2].zfill(2)
        res[1] = [dic[res[1]]][0]
        return "-".join(res[::-1])


# leetcode submit region end(Prohibit modification and deletion)

date1 = "20th Oct 2052"
x = Solution().reformatDate(date1)
print(x)
