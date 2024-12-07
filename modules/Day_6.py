from typing import Tuple
from modules.common import create_grid
from collections import defaultdict


# Directions to look for neighbors: right, diagonal-down-right, down, diagonal-down-left, left, diagonal-up-left, up, diagonal-up-right
LOOK_DIR = [(0, -1), (1, 0), (0, 1), (-1, 0)]
SYMB = ['|', '-', '|', '-']


def main(inputs: str) -> Tuple[int, int]:
    """
    Main function to solve the problem by finding valid positions of the words.
    """
    grid = create_grid(inputs.splitlines())  # Convert input into a grid
    nb_row = len(grid)  # Number of rows in the grid
    nb_col = len(grid[0])  # Number of columns in the grid
    pos_visited = defaultdict(list)
    new_block = set()

    def print_grid() -> None:
        for row in grid:
            print(''.join(row))
        print('\n')

    def pos_in_grid(x, y) -> bool:
        return 0 <= x < nb_col and 0 <= y < nb_row

    start = [(x, y) for y, row in enumerate(grid)
             for x, col in enumerate(row) if col == '^'][0]

    dx_dy = LOOK_DIR[0]
    x, y = start
    while pos_in_grid(x, y):
        if grid[y][x] != '#':
            grid[y][x] = SYMB[LOOK_DIR.index(dx_dy)] if (
                x, y) not in pos_visited.keys() else '+'
            pos_visited[(x, y)].append(dx_dy)
            if LOOK_DIR[(LOOK_DIR.index(dx_dy) + 1) % 4] in pos_visited[(x, y)]:
                block_x, block_y = x + dx_dy[0], y + dx_dy[1]
                new_block.add((block_x, block_y))
                grid[block_y][block_x] = "O"
                print_grid()
                pass
        else:
            x, y = x - dx_dy[0], y - dx_dy[1]
            grid[y][x] = "+"
            dx_dy = LOOK_DIR[(LOOK_DIR.index(dx_dy) + 1) % 4]
        print_grid()
        x, y = x + dx_dy[0], y + dx_dy[1]

    return len(pos_visited), len(new_block)
