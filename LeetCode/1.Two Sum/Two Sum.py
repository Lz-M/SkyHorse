def twosum(self, nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

nums = [2, 7, 11, 5]
target = 9
answer = twosum(target, nums)
print(answer)