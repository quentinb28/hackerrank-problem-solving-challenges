def solution(A):

    left_sum = A[0]

    right_sum = sum(A) - A[0]

    diff = abs(left_sum - right_sum)

    for i in range(1, len(A) - 1):

        left_sum += A[i]

        right_sum -= A[i]

        new_diff = abs(left_sum - right_sum)

        if new_diff < diff:

            diff = new_diff

    return diff


if __name__ == '__main__':

    A = [1, 2, 4, 5, 5, 6]

    solution(A)
