from advent_of_code import day03


def test_solve():
    # example 1
    input1 = "R8,U5,L5,D3"
    input2 = "U7,R6,D4,L4"
    assert day03.solve(inputs=(input1, input2)) == 6
    # example 2
    input1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    input2 = "U62,R66,U55,R34,D71,R55,D58,R83"
    assert day03.solve(inputs=(input1, input2)) == 159
    # example 3
    input1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    input2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    assert day03.solve(inputs=(input1, input2)) == 135
