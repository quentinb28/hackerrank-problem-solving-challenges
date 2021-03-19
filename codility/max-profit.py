def solution(A):

    global_max_sum = local_max_sum = 0

    for i in range(1, len(A)):

        d = A[i] - A[i - 1]  # compute diff between stock prices

        local_max_sum = max(d, local_max_sum + d)

        global_max_sum = max(local_max_sum, global_max_sum)

    return global_max_sum


if __name__ == '__main__':

    max_profits = [125, 45, 67, 8, 89, 34, 56, 78]

    solution(max_profits)
