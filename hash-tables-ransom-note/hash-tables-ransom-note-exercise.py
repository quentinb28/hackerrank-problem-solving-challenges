from collections import Counter

magazine = ['give', 'me', 'one', 'grand', 'today', 'night']
note = ['give', 'one', 'grand', 'today']


def checkMagazine(magazine, note):

    # Get intersection of both counters, magazine & note
    # Takes into account item counts
    c = list((Counter(magazine) & Counter(note)).elements())

    # Check if length of common words equals that of note
    if len(c) == len(note):

        print('Yes')

    else:

        print('No')


if __name__ == '__main__':

    checkMagazine(magazine, note)
