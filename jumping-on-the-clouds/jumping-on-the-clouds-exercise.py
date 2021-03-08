c = [0, 0, 0, 1, 0, 0]


def jumpingOnClouds(c):

    # Store the jumps count
    jumps_count = 0

    # Keep track of where the cursor is
    cursor = 0

    # Run while loop until the end of the list is reached
    while cursor != len(c) - 1:

        # Check there's enough space to avoid index error
        if cursor < len(c) - 2 and c[cursor + 2] != 1:

            # Make a jump of two clouds
            cursor += 2
            jumps_count += 1

        else:

            # Make a jump of one cloud
            cursor += 1
            jumps_count += 1

    return jumps_count


if __name__ == '__main__':

    r = jumpingOnClouds(c)

    print(r)
