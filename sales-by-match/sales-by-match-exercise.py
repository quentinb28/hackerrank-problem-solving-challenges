from collections import Counter

n = 7
ar = [1, 2, 1, 2, 3]


def sockMerchant(n, ar):
    
    matched_pairs = 0
    
    organized_socks = Counter(ar)
    
    for v in organized_socks.values():
        
        matched_pairs += v // 2
    
    return matched_pairs


if __name__ == "__main__":
    
    r = sockMerchant(n, ar)
    
    print(r)
