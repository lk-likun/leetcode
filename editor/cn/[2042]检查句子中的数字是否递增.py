# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        ls = list()
        for i in s.split(" "):
            if i.isdigit():
                ls.append(int(i))
        for i in range(len(ls)):
            for j in range(i + 1, len(ls)):
                if ls[j] < ls[i] or ls[j] == ls[i]:
                    return False
        return True


# leetcode submit region end(Prohibit modification and deletion)

s1 = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
Solution().areNumbersAscending(s1)
