# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        for num in nums:
            if count[num] > len(nums) / 2:
                return num
# leetcode submit region end(Prohibit modification and deletion)
