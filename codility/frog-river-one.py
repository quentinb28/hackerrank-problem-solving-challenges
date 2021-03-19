def solution(X, A):

    river_positions = [False] * (X + 1)

    for pos in A:

        if river_positions[pos] is False:

            river_positions[pos] = True

            X -= 1

        if X == 0:
            return A.index(pos)

    return -1


if __name__ == '__main__':

    X, A = 4, [1, 3, 3, 4, 4, 2, 3, 1, 1]  # 4

    solution(X, A)
