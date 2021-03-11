s1 = 'jackandjill'
s2 = 'wentupthehill'


def twoStrings(s1, s2):

    # Iterate through characters in s1
    for s in s1:

        # Print YES if character in s2
        if s in s2:
            return 'YES'

    return 'NO'


if __name__ == '__main__':

    r = twoStrings(s1, s2)

    print(r)
