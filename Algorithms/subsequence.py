def subsequence(arr, curr_idx, sub_arr, sub_curr_idx):
    if curr_idx >= len(arr):
        print(sub_arr)
        return
    subsequence(arr, curr_idx + 1, sub_arr, sub_curr_idx)
    sub_arr[sub_curr_idx] = arr[curr_idx]
    subsequence(arr, curr_idx+1, sub_arr, sub_curr_idx+1)

arr = [1,2,3]
sub_arr = [None] * len(arr)
subsequence(arr, 0, sub_arr, 0)