def clamp(_min: int, _max: int, x: int) -> int:
    return min(_max, max(_min, x))


def create_border(array: list[list[object]], wall: chr) -> list[list[object]]:
    for y in range(0, len(array)):
        for x in range(0, len(array[y])):
            if y == 0 or x == 0 or y == len(array) - 1 or x == len(array[y]) - 1:
                array[(x, y)] = wall
    return array
