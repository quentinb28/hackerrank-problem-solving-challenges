arr = [1, 3, 5, 2, 4, 6, 7]


def minimumSwaps(arr):

    swaps = 0

    index = 0

    # Run while loop until list is ordered
    while arr != sorted(arr):

        # Check if number is not what it should be: 1 on index 0
        if arr[index] != (index + 1):

            # Get index of number that should in current position
            index_right_number = arr.index(index + 1)

            # Swap with number in current position
            arr[index], arr[index_right_number] = arr[index_right_number], arr[index]

            swaps += 1

        index += 1

    return swaps


if __name__ == '__main__':

    r = minimumSwaps(arr)

    print(r)
