def solution(K, A):

    count = 0

    rope_length = 0

    for rope in A:

        rope_length += rope

        if rope_length >= K:

            count += 1

            rope_length = 0

    return count


if __name__ == '__main__':

    K, A = 4, [1, 2, 3, 4, 1, 1, 3]

    solution(K, A)
