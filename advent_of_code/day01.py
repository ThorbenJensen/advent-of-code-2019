""" https://adventofcode.com/2019/day/1 """

import math
from pathlib import Path

from functional import seq


INPUT: Path = Path("data/day01.txt")


def fuel_required(mass: int) -> int:
    """
    To find the fuel required for a module, take its mass, divide by three,
    round down, and subtract 2.
    Arguments:
        mass {float} -- mass of module
    Returns:
        int -- required fuel
    """
    required_fuel = math.floor(mass / 3) - 2
    return max(required_fuel, 0)


def fuel_required_recursively(mass: int) -> int:
    required_fuel = fuel_required(mass)
    if required_fuel == 0:
        return 0
    else:
        return required_fuel + fuel_required_recursively(required_fuel)


if __name__ == "__main__":
    # read input
    with open(str(INPUT)) as f:
        masses = f.readlines()
    # calculate fuel, simple
    sum_fuel = seq(masses).map(int).map(fuel_required).sum()
    print(f"Sum of required fuel: {sum_fuel}")
    # calculate fuel recursively
    sum_fuel_recursively = seq(masses).map(int).map(fuel_required_recursively).sum()
    print(f"Sum of required fuel, calculated recursively: {sum_fuel_recursively}")
