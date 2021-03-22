def solution(M, A):

    total_slices = 0

    head = 0

    # keep track of numbers currently in slice
    in_current_slice = [False] * (M + 1)

    # iterate through tails and advance head as much as possible for each tail
    for tail in range(len(A)):

        # advance head if still in list and not currently in slice
        while head < len(A) and (not in_current_slice[A[head]]):

            # specify head number is in slice
            in_current_slice[A[head]] = True

            # new count of slices equal the total number of numbers in slice when adding head
            total_slices += (head - tail) + 1

            # condition of count of slices exceed limit
            total_slices = 1000000000 if total_slices > 1000000000 else total_slices

            # advance head
            head += 1

        # tail no longer in currently in slice
        in_current_slice[A[tail]] = False

    return total_slices


M, A = 9, [2, 4, 1, 7, 6, 9, 7, 3, 5, 5, 8, 7, 1]

print(solution(M, A))
