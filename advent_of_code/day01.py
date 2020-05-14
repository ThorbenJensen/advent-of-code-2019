import math
from pathlib import Path

from functional import seq


INPUT: Path = Path("data/day01.txt")


def fuel_required_by_module(mass: int) -> int:
    """
    To find the fuel required for a module, take its mass, divide by three,
    round down, and subtract 2.
    Arguments:
        mass {float} -- mass of module
    Returns:
        int -- required fuel
    """
    return math.floor(mass / 3) - 2


if __name__ == "__main__":
    with open(str(INPUT)) as f:
        masses = f.readlines()

    sum_fuel = seq(masses).map(int).map(fuel_required_by_module).sum()

    print(f"Sum of required fuel: {sum_fuel}")
