def solution(A, B, K):

    if A % K != 0:

        A = K * (1 + A // K)

    if B % K != 0:

        B -= B % K

    return (B - A + K) // K


if __name__ == '__main__':

    A, B, K = 5, 16, 3  # 4

    solution(A, B, K)
