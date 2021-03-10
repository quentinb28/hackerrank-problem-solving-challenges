q = [2, 1, 5, 3, 4]


def minimumBribes(q):

    # Initiate total number of bribes
    total_bribes = 0

    #  Iterate through each runner backward
    for i in range(len(q) - 1, -1, -1):

        # Stop execution if a runner bribes more than two runners
        if q[i] - (i + 1) > 2:

            print('Too chaotic')
            return

        # Add the number of runners behind current runner that were bribed
        else:

            total_bribes += len(list(filter(lambda x: x < q[i], q[i + 1:])))

    print(total_bribes)


if __name__ == '__main__':

    minimumBribes(q)
