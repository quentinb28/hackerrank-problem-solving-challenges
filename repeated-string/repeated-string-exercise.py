s = 'abc'
n = 10


def repeatedString(s, n):

    # Base occurrences of 'a' in s
    occurrences_in_s = s.count('a')

    # Number of times s can fit in n
    n_s_floor_division = n // len(s)

    # Remainder after fitting as many s as possible in n
    n_s_remainder = n % len(s)

    # Add (Number of times s can fit in n) * (Base occurrences of 'a' in s)
    total_occurrences = n_s_floor_division * occurrences_in_s

    #  Add occurrences of 'a' in s for slice of remainder size
    total_occurrences += s[:n_s_remainder].count('a')

    return total_occurrences


if __name__ == '__main__':
    
    r = repeatedString(s, n)

    print(r)
