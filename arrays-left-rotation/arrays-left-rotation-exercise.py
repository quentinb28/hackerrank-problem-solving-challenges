a = [1,2,3,4,5]
d = 2


def rotLeft(a, d):
    
    # Run while loop until no iterations left
    while d > 0:
        
        # Add first element at the end
        a.append(a[0])
        
        # Delete first element
        del a[0]
        
        # Substract one iteration
        d -= 1
        
    return a


if __name__ == '__main__':
    
    r = rotLeft(a, d)
    
    print(r)

