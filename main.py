def twosum(nums, target):
    flags = False
    
    for i in range(len(nums)):
        a = nums[i]
        for j in range(len(nums)):
            if j == i:
                continue
            b = nums[j]
            c = a + b
            if target == c:
                flags = True
                break
        if flags:
            break
    return i, j

nums = [3, 2, 4]
target = 6
i, j = twosum(nums, target)
