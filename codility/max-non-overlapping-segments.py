def solution(A, B):

    #  A: starting indexes
    #  B: ending indexes
    #  Both need to be sorted by ending indexes in ascending order

    last_end_segment = -1

    chosen_count = 0

    for i in range(len(A)):

        if A[i] > last_end_segment:

            chosen_count += 1

            last_end_segment = B[i]

    return chosen_count


if __name__ == '__main__':

    A, B = [2, 4, 1, 7, 9, 9], [3, 5, 6, 8, 9, 10]

    # sorted(list(zip(A, B)), key=lambda x: x[1])

    print(solution(A, B))
