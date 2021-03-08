steps = 8
path = 'UDDDUDUUDD'


def countingValleys(steps, path):

    # Store valleys count
    valleys_count = 0

    # Keep track of state - True: Currently in Valley | False: Currently in Mountain
    state = 0

    # Iterate through path 'U' and 'D'
    for x in path:

        # Check if getting back from Valley
        if x == 'U' and state == -1:

            # Add one Valley
            valleys_count += 1
            state += 1

        # Check if going up
        elif x == 'U':

            state += 1

        # Check if going down
        elif x == 'D':

            state += -1

    return valleys_count


if __name__ == '__main__':

    r = countingValleys(steps, path)

    print(r)
