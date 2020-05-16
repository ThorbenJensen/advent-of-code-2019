from advent_of_code import day04


def test_is_within_range():
    assert not day04.is_within_range(42)
    assert not day04.is_within_range(-20)
    assert day04.is_within_range(246540)
    assert day04.is_within_range(787410)
    assert day04.is_within_range(787419)


def test_two_adjacent_digits_same():
    assert day04.two_adjacent_digits_same(111111)
    assert not day04.two_adjacent_digits_same(123456)


def test_digits_never_decrease():
    assert day04.digits_never_decrease(123456)
    assert day04.digits_never_decrease(123789)
    assert not day04.digits_never_decrease(222221)
