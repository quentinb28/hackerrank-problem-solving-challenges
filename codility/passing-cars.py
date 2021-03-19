# MY SOLUTION
def solution(A):

    passed_cars = 0

    east_cars = 0

    for i in range(len(A)):

        if A[i] == 0:

            east_cars += 1

        else:

            passed_cars += east_cars * 1

        if passed_cars > 1000000000:

            return -1

    return passed_cars


# COURSE SOLUTION
def solution(A):

    count = 0

    suffix_sum = [0] * (len(A) + 1)

    for i in range(len(A) - 1, -1, -1):

        suffix_sum[i] = A[i] + suffix_sum[i + 1]

        if A[i] == 0:

            count += suffix_sum[i]

        if count > 1000000000:

            return -1

    return count


if __name__ == '__main__':

    A = [0, 1, 0, 1, 1]

    solution(A)
