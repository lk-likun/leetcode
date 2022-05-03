# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        nums = list()
        letters = list()
        for i in logs:
            a, b = i.split(' ', 1)
            if str(b[0]).isdigit():
                nums.append(i)
            else:
                letters.append((" ".join(i.split(" ")[1:]), i.split(" ")[0]))
        letters.sort()
        return [letter[1] + " " + letter[0] for letter in letters] + nums


# leetcode submit region end(Prohibit modification and deletion)


logs1 = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
x = Solution().reorderLogFiles(logs1)
print(x)
