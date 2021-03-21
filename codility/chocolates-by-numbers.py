# MY SOLUTION (87%)
def solution(N, M):

    result = 0

    new_N = N

    while True:

        r = new_N % M

        if r == 0:

            result += new_N // M

            break

        else:

            result += 1 + new_N // M

        new_N = N - (M - r)

    return result


# COURSE SOLUTION
def find_gcd(A, B):

    if B == 0:

        return A

    else:

        # take B and rest of division of previous two numbers, A and B
        return find_gcd(B, A % B)


def solution(N, M):

    # get greatest common divisor (gcd)
    gcd = find_gcd(N, M)

    # compute least common multiple (lcm) with greatest common divisor (gcd)
    lcm = N * M // gcd

    # return result
    return lcm // M


if __name__ == '__main__':

    N, M = 10, 4

    solution(N, M)
