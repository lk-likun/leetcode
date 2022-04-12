def binarySort(nums):
    right = len(nums) - 1
    mid_index = right // 2
    if right <= 0:
        return nums
    tmp_left = list()
    tmp_right = list()
    tmp_mid = list()
    for i in range(len(nums)):
        if nums[i] < nums[mid_index]:
            tmp_left.append(nums[i])
        elif nums[i] > nums[mid_index]:
            tmp_right.append(nums[i])
        else:
            tmp_mid.append(nums[i])
    return binarySort(tmp_left) + tmp_mid + binarySort(tmp_right)


ls = [10, 1, 5, 4, 7, 6, 3]
x = binarySort(ls)
print(x)