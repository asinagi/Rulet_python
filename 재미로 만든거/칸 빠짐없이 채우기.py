def can_place(tile, wall, row, col):
    """
    Check if a tile can be placed at given position on the wall
    """
    height = len(tile)
    width = len(tile[0])

    if row + height > len(wall) or col + width > len(wall[0]):
        return False

    for i in range(height):
        for j in range(width):
            if tile[i][j] == 1 and wall[row + i][col + j] != 0:
                return False
    return True

def place_tile(tile, wall, row, col, tile_type):
    """
    Place a tile on the wall
    """
    height = len(tile)
    width = len(tile[0])

    for i in range(height):
        for j in range(width):
            if tile[i][j] == 1:
                wall[row + i][col + j] = tile_type

def remove_tile(tile, wall, row, col):
    """
    Remove a tile from the wall
    """
    height = len(tile)
    width = len(tile[0])

    for i in range(height):
        for j in range(width):
            if tile[i][j] == 1:
                wall[row + i][col + j] = 0

def find_empty_location(wall):
    """
    Find an empty location on the wall
    """
    for i in range(len(wall)):
        for j in range(len(wall[0])):
            if wall[i][j] == 0:
                return i, j
    return None, None

def fill_wall(wall, tiles, tile_count):
    """
    Fill the wall with tiles
    """
    empty_row, empty_col = find_empty_location(wall)
    if empty_row is None and empty_col is None:
        return True

    for tile_type, tile in enumerate(tiles, start=1):
        if tile_count[tile_type] > 0:
            if can_place(tile, wall, empty_row, empty_col):
                place_tile(tile, wall, empty_row, empty_col, tile_type)
                tile_count[tile_type] -= 1

                if fill_wall(wall, tiles, tile_count):
                    return True

                remove_tile(tile, wall, empty_row, empty_col)
                tile_count[tile_type] += 1

    return False

def print_wall(wall):
    """
    Print the wall
    """
    for row in wall:
        print(row)

if __name__ == "__main__":
    wall_height = 5
    wall_width = 10
    wall = [[0] * wall_width for _ in range(wall_height)]

    tiles = [
        [[1]],
        [[1, 1]],
        [[1], [1]],
        [[1, 1], [1, 1]],
        [[1, 1], [1, 1], [1, 1]]
    ]

    tile_count = {1: 3, 2: 2, 3: 0, 4: 3, 5: 3}

    if fill_wall(wall, tiles, tile_count):
        print_wall(wall)
    else:
        print("Cannot fill the wall with given tiles.")
