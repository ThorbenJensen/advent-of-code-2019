from pathlib import Path
from typing import List, Tuple

import numpy as np
from functional import seq

INPUT = Path("data/day03.txt")
CENTRAL_PORT = (16000, 8000)  # (row, column)


def input_to_directions(input: str) -> List[Tuple[str, int]]:
    input_list = input.split(",")
    directions = seq(input_list).map(lambda x: (x[0], int(x[1:])))
    return directions


def direction_to_vector(direction: Tuple[str, int]) -> Tuple[int]:
    direction_string = direction[0]
    if direction_string == "U":
        return (-1, 0)
    if direction_string == "D":
        return (1, 0)
    if direction_string == "R":
        return (0, 1)
    if direction_string == "L":
        return (0, -1)
    raise ValueError


def get_empty_grid() -> np.ndarray:
    grid = np.zeros(shape=tuple(e * 2 for e in CENTRAL_PORT))
    grid[CENTRAL_PORT] = 1
    return grid


def draw_wire(input: str) -> np.ndarray:
    grid = get_empty_grid()
    directions: List[Tuple[str, int]] = input_to_directions(input)
    position = CENTRAL_PORT
    for direction in directions:
        vector = direction_to_vector(direction)
        # print(vector)
        for i in range(direction[1]):
            position = [position[i] + vector[i] for i in range(len(position))]
            # print(position)
            grid[(position[0], position[1])] = 1
    return grid


def manhattan_distance(port: Tuple[int, int]):
    return abs(CENTRAL_PORT[0] - port[0]) + abs(CENTRAL_PORT[1] - port[1])


def combined_wiring(inputs: Tuple[str]):
    wiring1 = draw_wire(input=inputs[0])
    wiring2 = draw_wire(input=inputs[1])
    wiring_combined = wiring1 + wiring2
    return wiring_combined


def manhattan_distance_closest_crossing(grid_combined: np.ndarray):
    crossings = seq((zip(*np.where(grid_combined > 1)))).filter(
        lambda x: x != CENTRAL_PORT
    )
    closest_distance = crossings.map(manhattan_distance).min()
    return closest_distance


def solve_manhattan_distance(inputs: Tuple[str]):
    grid_combined = combined_wiring(inputs=(inputs[0], inputs[1]))
    closest_distance = manhattan_distance_closest_crossing(grid_combined)
    return closest_distance


if __name__ == "__main__":
    # read input
    with open(str(INPUT)) as f:
        inputs = tuple(f.readlines())
    closest_distance = solve_manhattan_distance(inputs=inputs)
    print(f"manhattan distance of closes crossing: {closest_distance}")
