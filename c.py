def puede_llegar(nums):
    n = len(nums)
    max_alcanzable = 0

    for i in range(n):
        if i > max_alcanzable:
            return False
        max_alcanzable = max(max_alcanzable, i + nums[i])
        if max_alcanzable >= n - 1:
            return True
        
    return False

