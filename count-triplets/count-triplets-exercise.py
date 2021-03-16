arr, r = [1, 3, 3, 9, 9, 27, 81], 3


def countTriplets(arr, r):

    # initialize total count of triplets
    count = 0

    # initialize dictionary of all values
    dict = {}

    # initialize dictionary of pairs
    dictPairs = {}

    # iterate through reversed list
    for i in reversed(arr):

        # store value multiple count in dictionary of pairs
        if i * r in dict:

            dictPairs[i] = dictPairs.get(i, 0) + dict[i * r]

        # add to count when value multiple already in dictionary of pairs
        if i * r in dictPairs:

            count += dictPairs[i * r]

        # add value to dictionary of all values, create if it does not exist yet
        dict[i] = dict.get(i, 0) + 1

    return count


if __name__ == '__main__':

    r = countTriplets(arr, r)

    print(r)
