# 13. RO‘YXATNI SARALASH (sortsiz)
nums = [int(x) for x in input().split()]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
print(nums)
