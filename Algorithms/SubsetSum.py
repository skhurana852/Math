arr = [5,2,1,3]
m = 9
dp_arr = [[]]
for i in range(len(arr)+1):
    for j in range(m+1):
        dp_arr[i][j] = False


def solve():
    for i in range(len(arr)+1):
        dp_arr[i][0] = True
    
    for row in range(1, len(arr)+1):
        for col in range(1, m+1):
            if col < arr[row-1]:
                dp_arr[row][col] = dp_arr[row-1][col]
            else:
                if dp_arr[row-1][col]:
                    dp_arr[row][col] = dp_arr[row-1][col]
                else:
                    dp_arr[row][col] = dp_arr[row-1][col-arr[row]]
    
    if not dp_arr[len(arr)][m]:
        print("not feasible")
    
    col_idx = m
    row_idx = len(arr)

    result = []

    while col_idx >0 or row_idx > 0:
        if dp_arr[row_idx][col_idx] == dp_arr[row_idx-1][col_idx]:
            row_idx -= 1
        else:
            result.append(dp_arr[row_idx][col_idx])
            col_idx = col_idx - arr[row_idx-1]
            row_idx = row_idx-1

