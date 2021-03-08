steps = 8
path = 'UDDDUDUUDD'


def countingValleys(steps, path):

    valleys_count = 0

    state = 0

    for x in path:

        if x == 'U' and state == -1:

            valleys_count += 1
            state += 1

        elif x == 'U':

            state += 1

        elif x == 'D':

            state += -1

    return valleys_count


if __name__ == '__main__':
    r = countingValleys(steps, path)

    print(r)
