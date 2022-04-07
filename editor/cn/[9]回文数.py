# leetcode submit region begin(Prohibit modification and deletion)
import os


def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    if str(x)[::-1] == str(x):
        return True
    else:
        return False


class Solution:
    n = isPalindrome(4321)
    print(n)
# leetcode submit region end(Prohibit modification and deletion)
