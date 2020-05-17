from advent_of_code import day01


def test_fuel_required():
    assert day01.fuel_required(12) == 2
    assert day01.fuel_required(14) == 2
    assert day01.fuel_required(1969) == 654
    assert day01.fuel_required(100756) == 33583


def test_fuel_required_recursively():
    assert day01.fuel_required_recursively(1969) == 966
    assert day01.fuel_required_recursively(100756) == 50346
