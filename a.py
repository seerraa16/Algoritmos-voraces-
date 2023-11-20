def max_area(height):
    n = len(height)
    max_area = 0
    left, right = 0, n - 1

    while left < right:
        # Calcular el ancho del recipiente
        width = right - left

        # Calcular la altura del recipiente (tomar la menor altura entre las dos líneas)
        h = min(height[left], height[right])

        # Actualizar el área máxima si es necesario
        max_area = max(max_area, width * h)

        # Mover los índices hacia el centro
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area