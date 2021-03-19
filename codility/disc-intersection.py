class DiscLog:

    def __init__(self, x, startend):

        self.x = x

        self.startend = startend


def solution(A):

    DiscHistory = []

    for i in range(len(A)):

        DiscHistory.append(DiscLog(i - A[i], 1))

        DiscHistory.append(DiscLog(i + A[i], -1))

    DiscHistory.sort(key=lambda d: (d.x, -d.startend))

    intersections = 0

    current_state = 0

    for d in DiscHistory:

        current_state += d.startend

        if d.startend == 1:

            intersections += current_state - 1

    if intersections > 10000000:

        return -1

    return intersections


if __name__ == '__main__':

    A = [1, 5, 2, 1, 4, 0]

    solution(A)
