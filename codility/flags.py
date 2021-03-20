def solution(A):

    # initialize list of peaks indexes in between peaks
    peaks = [0] * len(A)

    # last item should be index outside of peaks length
    next_peak = len(A)

    peaks[-1] = next_peak

    # stops at 0 because we want to avoid index out of range within if statement
    for i in range(len(A) - 2, 0, -1):

        # if height greater than point before and after then save peak index
        if (A[i] > A[i - 1]) and (A[i] > A[i + 1]):

            next_peak = i

        # keep saving peak index until next peak occurs
        peaks[i] = next_peak

    # cannot be within loop for index out of bound reasons
    peaks[0] = next_peak

    current_guess = 0

    next_guess = 0

    # iterate through flags counts until it breaks
    while can_place_flags(peaks, next_guess):

        # saves last working flags count
        current_guess = next_guess

        next_guess += 1

    return current_guess


def can_place_flags(peaks, flags_to_place):

    # to land on index 1 after first iteration (cannot land on index 0)
    current_position = 1 - flags_to_place

    # iterates through each flag and add the relevant number of places to next position
    for i in range(flags_to_place):

        # if next flag falls outside of peaks index range
        if current_position + flags_to_place > len(peaks) - 1:
            return False

        # current position moves to current position + flags places
        current_position = peaks[current_position + flags_to_place]

    # if last current position within peaks size then return True
    return current_position < len(peaks)


if __name__ == '__main__':

    A = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]

    solution(A)
