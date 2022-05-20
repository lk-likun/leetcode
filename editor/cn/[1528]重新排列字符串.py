# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # dic = dict(zip(indices, s))
        # res = list(dict(sorted(dic.items(), key=lambda z: z[0])).values())
        # return "".join(res)

        res = [0] * len(s)
        for i, v in enumerate(s):
            res[indices[i]] = v
        return "".join(res)


# leetcode submit region end(Prohibit modification and deletion)

s1 = "codeleet"
indices1 = [4, 5, 6, 7, 0, 2, 1, 3]
x = Solution().restoreString(s1, indices1)
print(x)
