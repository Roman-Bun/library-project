def two_sum_slow(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

print(two_sum_slow([2, 7, 11, 15], 9))