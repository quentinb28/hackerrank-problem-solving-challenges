def solution(A):

    candidate = 0

    consecutive_occurrences = 0

    for c in A:

        if consecutive_occurrences == 0:

            candidate = c

            consecutive_occurrences += 1

        elif c != candidate:

            consecutive_occurrences -= 1

        else:

            consecutive_occurrences += 1

    if A.count(candidate) > (len(A) / 2):

        return A.index(candidate)

    else:

        return -1


if __name__ == '__main__':

    A = [3, 2, 2, 3, 3]

    solution(A)
