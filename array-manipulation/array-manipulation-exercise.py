n = 10
queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]


def arrayManipulation(n, queries):
    """
    The idea to optimize the code using the prefix sum principle.
    The objective is to manipulate values only where it can be useful and avoid unnecessary computations.
    Adding k in the first position and subtracting k to the last position + 1 favors the use of the prefix sum.
    :param n: Length of array.
    :param queries: List of queries.
    :return: Max value after operations.
    """

    # Initiate zeros list of size n
    final_array = [0] * n

    # Iterate through queries
    for [a, b, k] in queries:

        #  Add k value in first position  in final array specified in query
        final_array[a - 1] += k

        # Subtract k value to last position + 1 in final array specified in query (avoid index out of bound)
        if b < n:
            final_array[b] -= k

    max_value = 0
    last = final_array[0]

    # Compute last value, which equals to last value + current value in final array
    for i in range(1, len(final_array)):

        last += final_array[i]

        if last > max_value:
            max_value = last

    return max_value
