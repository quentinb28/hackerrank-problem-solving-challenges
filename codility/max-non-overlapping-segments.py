def solution(A, B):

    last_end_segment = -1

    chosen_count = 0

    for i in range(len(A)):

        if A[i] > last_end_segment:

            chosen_count += 1

            last_end_segment = B[i]

    return chosen_count


if __name__ == '__main__':

    # Doubt with the case below, the code does not take that case into account - check answer in Q&A
    # A, B = [1, 2, 3, 7, 9, 9], [5, 3, 6, 8, 9, 10]

    A, B = [1, 3, 7, 9, 9], [5, 6, 8, 9, 10]

    solution(A, B)
