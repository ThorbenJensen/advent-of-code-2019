from copy import copy
from typing import List, Tuple

import numpy as np
from functional import seq

CENTRAL_PORT = (10, 10)  # (row, column)


def input_to_directions(input: str) -> List[Tuple[str, int]]:
    input_list = input.split(",")
    directions = seq(input_list).map(lambda x: (x[0], int(x[1:])))
    return directions


def vector_for_direction(direction: Tuple[str, int]) -> Tuple[int]:
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


def draw_wire(field: np.ndarray, input: str) -> np.ndarray:
    directions: List[Tuple[str, int]] = input_to_directions(input)
    field_wire = copy(field)
    position = CENTRAL_PORT
    for direction in directions:
        vector = vector_for_direction(direction)
        # print(vector)
        for i in range(direction[1]):
            position = [position[i] + vector[i] for i in range(len(position))]
            # print(position)
            field_wire[(position[0], position[1])] = 1
    return field_wire


a = np.zeros(shape=tuple(e * 2 for e in CENTRAL_PORT))
a[CENTRAL_PORT] = "1"


input1 = "R8,U5,L5,D3"
input2 = "U7,R6,D4,L4"

wiring1 = draw_wire(field=a, input=input1)
wiring2 = draw_wire(field=a, input=input2)

wiring = wiring1 + wiring2
print(wiring)

crossings = seq((zip(*np.where(wiring > 1)))).filter(lambda x: x != CENTRAL_PORT)


def manhattan_distance(port: Tuple[int, int]):
    return (abs(CENTRAL_PORT[0] - port[0]) + abs(CENTRAL_PORT[1] - port[1]))


closest_distance = crossings.map(manhattan_distance).min()
print(f"closest_distance: {closest_distance}")
