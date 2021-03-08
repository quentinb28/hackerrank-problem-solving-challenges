from collections import Counter

n = 7
ar = [1, 2, 1, 2, 3]


def sockMerchant(n, ar):

    # Store matched pairs
    matched_pairs = 0

    # Make counter of socks: {sock_type: count}
    sock_counter = Counter(ar)

    # Iterate through values of sock counter
    for v in sock_counter.values():

        # Add floor division of sock values to matched pairs - remainders are unmatched
        matched_pairs += v // 2
    
    return matched_pairs


if __name__ == "__main__":
    
    r = sockMerchant(n, ar)
    
    print(r)
