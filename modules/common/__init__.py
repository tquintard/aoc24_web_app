from typing import List


def create_grid(inputs: List):
    grid = list()
    for line in inputs:
        grid.append(list(line))
    return grid


def pos_in_grid(x: int, y: int, nb_col: int, nb_row: int) -> bool:
    """ Check if the position (x, y) is within the bounds of the grid """
    return 0 <= x < nb_col and 0 <= y < nb_row
