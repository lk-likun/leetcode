# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    @staticmethod
    def maxSubArray(nums):
        # if not nums:
        #     return -10 ** 4
        # if len(nums) == 1:
        #     return nums[0]
        # mid_index = len(nums) // 2
        # res = nums[mid_index]
        # res_bak = nums[mid_index]
        # for i in range(mid_index):
        #     l_index = mid_index - (i + 1)
        #     res_bak += nums[l_index]
        #     if res_bak > res:
        #         res = res_bak
        # res_bak = res
        # for i in range(mid_index):
        #     r_index = mid_index + (i + 1)
        #     if r_index < len(nums):
        #         res_bak += nums[r_index]
        #         if res_bak > res:
        #             res = res_bak
        # return max(Solution.maxSubArray(nums[:mid_index]), Solution.maxSubArray(nums[mid_index + 1:]), res)
        res = -10 ** 4
        tmp = 0
        for n in nums:
            if tmp + n > n:
                tmp += n
            else:
                tmp = n
            if tmp > res:
                res = tmp
        return res

# leetcode submit region end(Prohibit modification and deletion)

# ls = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Solution.maxSubArray(ls)
