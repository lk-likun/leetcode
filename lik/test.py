# a = 4.565
# b = int((a * 100 + 0.5)) / 100
# print(b)
class Solution:
    def quicksort(self, nums):
        if len(nums) < 2:
            return nums
        mid = nums[0]
        left = [i for i in nums[1:] if i <= mid]
        right = [i for i in nums[1:] if i > mid]
        return self.quicksort(left) + [mid] + self.quicksort(right)


ls = [1, 4, 2, 3, 6, 8, 4, 3, 5, 31, 6, 9]
x = Solution().quicksort(ls)
print(x)
