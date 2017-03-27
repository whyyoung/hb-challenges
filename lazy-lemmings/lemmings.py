"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""
    max_distance = 0

    if len(cafes) == num_holes:
        return max_distance
    elif len(cafes) == 1:
        max_distance = num_holes - 1
        return max_distance
    else:
        max_distance = min(cafes)
        i = 0
        while i < len(cafes) - 1:
            if max_distance < (cafes[i+1] - cafes[i])/2:
                max_distance = (cafes[i+1] - cafes[i])/2
            i += 1
        return max_distance

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; GREAT JOB!\n"
