arr = [[-1, -1, 0, -9, -2, -2],
       [-2, -1, -6, -8, -2, -5],
       [-1, -1, -1, -2, -3, -4],
       [-1, -9, -2, -4, -4, -5],
       [-7, -3, -3, -2, -9, -9],
       [-1, -3, -1, -2, -4, -5]]


def hourglassSum(arr):

    # Set final result to None 
    hourglass_sum_max = None

    # Determine row indexes limit
    row_indexes = len(arr) - 2

    # Determine col indexes limit
    col_indexes = len(arr[0]) - 2

    # Iterate through row limit
    for r in range(row_indexes):

        # Iterate through col limit
        for c in range(col_indexes):

            # Compute hourglass sum
            hourglass_sum = arr[r][c] + arr[r][c+1] + arr[r][c+2] + arr[r+1][c+1] + arr[r+2][c] + arr[r+2][c+1] + arr[r+2][c+2]
            
            # Assign to hourglass sum to final result if first iteration
            if hourglass_sum_max == None:
                
                hourglass_sum_max = hourglass_sum

            # Assign hourglass sum to final result if greater than current hourglass sum
            elif hourglass_sum > hourglass_sum_max:
                
                hourglass_sum_max = hourglass_sum
                
    return hourglass_sum_max


if __name__ == '__main__':
    
    r = hourglassSum(arr)
    
    print(r)

