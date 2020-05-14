from advent_of_code.day01 import fuel_required_by_module


def test_fuel_required_by_module():
    assert fuel_required_by_module(12) == 2
    assert fuel_required_by_module(14) == 2
    assert fuel_required_by_module(1969) == 654
    assert fuel_required_by_module(100756) == 33583
