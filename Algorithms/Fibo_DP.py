# Top Down Dynamic Programming = Recursion + Memoization
def fibonnaci(n, dp_arr):
    if n==0 or n==1:
        dp_arr[n] = n
        return n
    #already stored
    if dp_arr[n] != -1:
        return dp_arr[n]
    else:
        #compute and store
        dp_arr[n] = fibonnaci(n-1, dp_arr) + fibonnaci(n-2, dp_arr) #memoization
        return dp_arr[n]



#Bottom Up Dynamic Programming Approach = Iterative Approach

def fib_bottom_up_dp(n):
    dp_arr = []
    dp_arr.append(0)
    dp_arr.append(1)
    for i in range(2, n+1):
        dp_arr[i] = dp_arr[i-1] + dp_arr[i-2]
    
    return dp_arr[n]



dp_arr = []
for i in range(100):
    dp_arr.append(-1)
print(fibonnaci(5, dp_arr))
print(fib_bottom_up_dp(5))