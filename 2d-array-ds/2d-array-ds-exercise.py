arr = [[-1, -1, 0, -9, -2, -2],
       [-2, -1, -6, -8, -2, -5],
       [-1, -1, -1, -2, -3, -4],
       [-1, -9, -2, -4, -4, -5],
       [-7, -3, -3, -2, -9, -9],
       [-1, -3, -1, -2, -4, -5]]


def hourglassSum(arr):
    
    hourglass_sum_max = None
    
    row_indexes = len(arr) - 2
    
    col_indexes = len(arr[0]) - 2
    
    for r in range(row_indexes):
        
        for c in range(col_indexes):
            
            hourglass_sum = arr[r][c] + arr[r][c+1] + arr[r][c+2] + arr[r+1][c+1] + arr[r+2][c] + arr[r+2][c+1] + arr[r+2][c+2]
            
            if hourglass_sum_max == None:
                
                hourglass_sum_max = hourglass_sum
            
            elif hourglass_sum > hourglass_sum_max:
                
                hourglass_sum_max = hourglass_sum
                
    return hourglass_sum_max


if __name__ == '__main__':
    
    r = hourglassSum(arr)
    
    print(r)

