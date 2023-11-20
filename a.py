def max_area(height):
    n = len(height)
    max_area = 0
    left, right = 0, n - 1

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_area = max(max_area, width * h)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area