def solution(A, B):

    survivors = 0

    stack = []

    for i in range(len(A)):

        weight = A[i]

        if B[i] == 1:

            stack.append(weight)

        else:

            weightdown = stack.pop() if stack else -1

            while weightdown != -1 and weightdown < weight:

                weightdown = stack.pop() if stack else -1

            if weightdown == -1:

                survivors += 1

            else:

                stack.append(weightdown)

    return survivors + len(stack)


if __name__ == '__main__':

    A, B = [4, 3, 2, 1, 5], [0, 1, 0, 0, 0]

    solution(A, B)
