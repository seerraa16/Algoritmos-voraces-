def min_swaps_to_arrange_couples(row):
   
    pos_map = {x: i for i, x in enumerate(row)}

    def is_adjacent(x, y):
        return abs(x - y) == 1

    def swap(pos1, pos2):
        row[pos1], row[pos2] = row[pos2], row[pos1]
        pos_map[row[pos1]], pos_map[row[pos2]] = pos_map[row[pos2]], pos_map[row[pos1]]

    swaps = 0
    n = len(row) // 2

    for i in range(0, len(row), 2):
        couple = row[i]
        partner = couple + 1 if couple % 2 == 0 else couple - 1

        if not is_adjacent(pos_map[couple], pos_map[partner]):
            swap(pos_map[couple], pos_map[partner])
            swaps += 1

    return swaps

row = [0, 2, 1, 3, 4, 6, 5, 7]
result = min_swaps_to_arrange_couples(row)
print(f"Número mínimo de intercambios: {result}")
