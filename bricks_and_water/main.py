def get_water_between_boundaries(bricks_array):
    """ Compute water on the inside of a brick array

    It is assumed that no inner brick is higher than any of the boundary bricks.

    Compute the potential amount of water. This is the height of the lower one of the border bricks times the
    number of blocks inside.

    From this we have to remove the number of actual blocks inside

    Parameters
    ----------
    bricks_array: list
        number array representing bricks

    Returns
    -------
    int
        number of water blocks held by this brick array
    """
    effective_height = min(bricks_array[0], bricks_array[-1])
    potential_water_amount = effective_height * (len(bricks_array) - 2)
    obstacles = sum(bricks_array[1:-1])

    return potential_water_amount - obstacles


def how_much_water2(bricks_array):
    """ Compute the number of water bricks in an arbitrary array

    The basic idea is that we find the positions of the two largest columns and determine the amount of water inside
    this array. For this we can use the function ``get_water_between_boundaries``.

    Afterwards we replace the entire sub-array by its right boundary since we know that it must be bigger or equal to
    any other brick in the array.

    Parameters
    ----------
    bricks_array

    Returns
    -------

    """

    total_water_amount = 0

    while True:
        if len(bricks_array) < 3:
            break

        temp = bricks_array.copy()
        temp.sort(reverse=True)
        highest, second_highest = temp[0:2]

        position_highest = bricks_array.index(highest)
        # check for second highest right of highest, else it must be left of it
        try:
            position_second_highest = bricks_array.index(second_highest, position_highest + 1)
        except ValueError:
            position_second_highest = bricks_array.index(second_highest, 0, position_highest + 1)

        left_boundary = min(position_highest, position_second_highest)
        right_boundary = max(position_highest, position_second_highest)

        # get water inside boundaries
        water_inside = get_water_between_boundaries(bricks_array[left_boundary:right_boundary + 1])
        total_water_amount += water_inside
        del bricks_array[left_boundary:right_boundary]

    return total_water_amount


def how_much_water(bricks_array: list) -> int:
    water = 0
    heightmax = 0
    for i in range(len(bricks_array)):
        if(heightmax < bricks_array[i]):
            heightmax = bricks_array[i]
        else:
            nextmax = max(bricks_array[i:])
            if(nextmax > bricks_array[i]):
                water += min(nextmax, heightmax)-bricks_array[i]
    return water


if __name__ == '__main__':
    bricks_array = [5,0,3,0,1]
