from collections import Counter
from itertools import combinations


s = 'ifailuhkqq'


def sherlockAndAnagrams(s):

    # Variable to store all possible combinations
    all_combinations = []

    # Iterate through substrings starting points
    for i in range(0, len(s) + 1):

        # Iterate through substrings ending points
        for j in range(1, len(s) + 1):

            # Append substring to list of combinations
            all_combinations.append(s[i:j])

    # Sort all substrings so the anagrams can be counted
    all_combinations = [''.join(sorted(c)) for c in all_combinations]

    # Filter out all empty strings
    all_combinations = list(filter(None, all_combinations))

    result = 0

    # Get the values from the counter and compute all the possible anagram pairs
    # (i.e. if v = 4 then the options are 1-2 1-3 1-4 2-3 2-4 3-4 = 6)
    for k, v in Counter(all_combinations).items():

        result += len(list(combinations(range(v), 2)))

    return result


if __name__ == '__main__':

    r = sherlockAndAnagrams(s)

    print(r)
