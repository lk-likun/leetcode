# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    @staticmethod
    def removeDuplicates(nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
# leetcode submit region end(Prohibit modification and deletion)
