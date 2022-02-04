n= 4
#ladder top down approach
def ladder(n, dp_arr):
    if n==0:
        return 1
    if n<0:
        return 0
    if dp_arr[n] != -1:
        return dp_arr[n]
    else:
        dp_arr[n] = ladder(n-1, dp_arr)+ladder(n-2, dp_arr)+ladder(n-3, dp_arr)
        return dp_arr[n]

dp_arr = []
for i in range(1000):
    dp_arr.append(-1)

#ladder bottom up dp:
def ladder_bottom_up(n, k):
    ans = 0
    if n==0:
        return 1
    if n<0:
        return 0
    for i in range(1, k+1):
        ans += ladder_bottom_up(n-i, k)
    return ans
print(ladder_bottom_up(4, 3))