def solution(A, K):

    result = [None] * len(A)

    for i in range(len(A)):

        # if (i + K) < len(A), then modulo yields (i + K) else repeats within A's index range
        result[(i + K) % len(A)] = A[i]

    return result


if __name__ == '__main__':

    A, K = [2, 3, 4, 5], 5

    solution(A, K)
