def minion_game(s):
    """
    Input is a string.
    Both players attempt to make as many words as possible.
    One with words starting with a vowel.
    Another with words starting with consonants.
    :param s:
    :return:
    """

    # Function checks if letter is a vowel
    def is_vowel(x):
        vowels = ["A", "E", "I", "O", "U"]
        if x in vowels:
            return True
        return False

    kevin_counter = 0
    stuart_counter = 0

    # Adds all possibilities starting with current letter
    for i in range(len(s)):
        if is_vowel(s[i]):
            kevin_counter += (len(s) - i)
        else:
            stuart_counter += (len(s) - i)

    if kevin_counter > stuart_counter:
        print("Kevin", kevin_counter)
    elif stuart_counter > kevin_counter:
        print("Stuart", stuart_counter)
    else:
        print("Draw")


if __name__ == "__main__":

    string = "BANANA"

    minion_game(string)
