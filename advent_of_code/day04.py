import itertools

from functional import seq

START = 246540
END = 787419


def is_within_range(number: int) -> bool:
    if (number >= START) and (number <= END):
        return True
    else:
        return False


def two_adjacent_digits_same(number: int) -> bool:
    if str(number)[0] == str(number)[1]:
        return True
    if str(number)[1] == str(number)[2]:
        return True
    if str(number)[2] == str(number)[3]:
        return True
    if str(number)[3] == str(number)[4]:
        return True
    if str(number)[4] == str(number)[5]:
        return True
    return False


def matching_group_length_2(number: int) -> bool:
    lengths = [len(list(g)) for k, g in itertools.groupby(str(number))]
    return seq(lengths).filter(lambda x: x > 1).map(lambda x: x < 3).any()


def digits_never_decrease(number: int) -> bool:
    if str(number)[0] > str(number)[1]:
        return False
    if str(number)[1] > str(number)[2]:
        return False
    if str(number)[2] > str(number)[3]:
        return False
    if str(number)[3] > str(number)[4]:
        return False
    if str(number)[4] > str(number)[5]:
        return False
    return True


if __name__ == "__main__":
    candidates = seq(range(START, END + 1))

    passwords_one = (
        candidates.filter(is_within_range)
        .filter(two_adjacent_digits_same)
        .filter(digits_never_decrease)
    )

    print(f"number of possible passwords (part 1): {passwords_one.len()}")

    passwords_two = passwords_one.filter(matching_group_length_2)

    print(f"number of possible passwords (part 1): {passwords_two.len()}")
