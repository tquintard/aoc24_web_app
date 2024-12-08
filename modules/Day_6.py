from typing import Tuple, List
from modules.common import create_grid

# Directions for neighbor look-up: up, right, down, left
LOOK_DIR = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def main(inputs: str) -> Tuple[int, int]:
    # Create a 2D grid from the input
    grid = create_grid(inputs.splitlines())
    nb_row, nb_col = len(grid), len(grid[0])

    # Initialize sets to track visited positions and directions
    pos_dir_visited, pos_visited = set(), set()

    # Find the starting position (first occurrence of '^')
    start = next((x, y) for y, row in enumerate(grid)
                 for x, col in enumerate(row) if col == '^')

    def next_direction(current_dir: Tuple, directions: List[Tuple]) -> Tuple:
        """
        Get the next direction in a cyclic list of directions.
        """
        return directions[(directions.index(current_dir) + 1) % len(directions)]

    def walk(x: int, y: int, dx_dy: Tuple[int, int]) -> int:
        """
        Traverse the grid starting from (x, y) in the given direction `dx_dy`.
        Handles direction cycling and checks for visited positions.
        Stop once the walk get you out of the grid.
        """
        while 0 <= x < nb_col and 0 <= y < nb_row:
            # If the cell is not blocked
            if grid[y][x] != '#':
                pos_visited.add((x, y))  # Mark the cell as visited

                # Check if the position and direction have already been visited
                if (x, y, dx_dy) in pos_dir_visited:
                    return 1  # Loop detected
                # Mark position-direction as visited
                pos_dir_visited.add((x, y, dx_dy))
            else:
                # Block encountered: reverse and change direction
                x, y = x - dx_dy[0], y - dx_dy[1]
                dx_dy = next_direction(dx_dy, LOOK_DIR)

            # Move to the next position
            x, y = x + dx_dy[0], y + dx_dy[1]
        return 0

    # Part 1: Perform the initial guard walk and record visited positions
    walk(*start, LOOK_DIR[0])
    sol1 = len(pos_visited)

    # Part 2: Iterate through all visited positions and block each one
    sol2 = 0
    for x_block, y_block in pos_visited:
        # Reset visited sets for each blocked position
        pos_dir_visited, pos_visited = set(), set()

        # Temporarily block the cell and walk again
        grid[y_block][x_block] = "#"
        sol2 += walk(*start, LOOK_DIR[0])

        # Restore the grid to its original state
        grid[y_block][x_block] = "."

    return sol1, sol2
