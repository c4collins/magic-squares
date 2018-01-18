"""
3x3 Magic Square Generator
"""

import itertools

def convert_array_to_square(arr):
    assert len(arr) == 9
    return [
        [x for x in arr[:3]],
        [x for x in arr[3:6]],
        [x for x in arr[6:9]]
    ]

def is_magic(square):
    target = sum(square[0]) # row 1
    try:
        assert sum(square[1]) == target # row 2
        assert sum(square[2]) == target # row 3
        assert sum([square[0][0], square[1][0], square[2][0]]) == target # col 1
        assert sum([square[0][1], square[1][1], square[2][1]]) == target # col 2
        assert sum([square[0][2], square[1][2], square[2][2]]) == target # col 3
        assert sum([square[0][0], square[1][1], square[2][2]]) == target # diagonal \
        assert sum([square[2][0], square[1][1], square[0][2]]) == target # diagonal /
    except AssertionError:
        return False
    return True

def deconstruct_square_to_array(square):
    return ",".join(
        [str(x) for x in square[0]]
        + [str(x) for x in square[1]]
        + [str(x) for x in square[2]]
    )

def is_rotation_of_existing_magic_square(square, row1s):
    # We can eliminate all squares which are rotations or mirrors of one another
    # How many ways can this be done for a 3x3 square?
    # These are the results given when you don't remove duplicates for 1-9
    # 276 294 438 492 618 672 816 834
    # 951 753 951 357 753 159 357 159
    # 438 618 276 816 294 834 492 672
    # They are all the same:
    # 1: row1: 276
    # 2: col1: 276
    # 3: row3: 276
    # 4: col3: 276
    # 5: col1: 672
    # 6: row1: 672
    # 7: col3: 672
    # 8: row3: 672
    # You can do this with every row or column, and you'll see they're rotations and mirrors of one square
    # But since we can prove these are all the same, all you need to check is the rotations and mirrors or the first row

    square_row1 = square[0]
    square_row3 = square[2]
    col1 = [square[0][0], square[1][0], square[2][0]]
    col3 = [square[0][2], square[1][2], square[2][2]]

    for row1 in row1s:
        if col1 == row1 or list(reversed(col1)) == row1 \
            or col3 == row1 or list(reversed(col3)) == row1 \
            or square_row1 == row1 or list(reversed(square_row1)) == row1 \
            or square_row3 == row1 or list(reversed(square_row3)) == row1:
                return True # True = is_rotation

    return False # False = not is_rotation

if __name__ == "__main__":
    num_range = [x for x in range(9, 0, -1)]
    row1s = []
    for x in itertools.permutations(num_range, 9):
        square = convert_array_to_square(x)
        is_rotation = is_rotation_of_existing_magic_square(square, row1s)

        if not is_rotation and is_magic(square):
            print("{} is magic.".format(square))
            row1s.append(square[0])
            with open('results/magic-squares|1-{}.csv'.format(len(num_range)), 'a') as results_file:
                results_file.write(deconstruct_square_to_array(square) + "\n")

