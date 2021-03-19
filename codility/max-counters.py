def solution(N, A):

    counters = [0] * N

    startline = 0

    current_max = 0

    for i in A:

        x = i - 1

        if i > N:

            startline = current_max

        elif counters[x] < startline:

            counters[x] = startline + 1

        else:

            counters[x] += 1

        if i <= N and counters[x] > current_max:

            current_max = counters[x]

    for i in range(0, len(counters)):

        if counters[i] < startline:

            counters[i] = startline

    return counters


if __name__ == '__main__':

    N, A = 5, [3, 4, 4, 6, 1, 4, 4]

    solution(N, A)
