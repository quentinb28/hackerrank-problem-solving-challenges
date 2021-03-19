def solution(A):

    actual_sum = 0

    for number in A:

        actual_sum += number

    max_number = len(A) + 1

    expected_sum = max_number * (max_number + 1) // 2

    return expected_sum - actual_sum


if __name__ == '__main__':

    A = [2, 3, 1, 5]

    solution(A)
