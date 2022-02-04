arr = [40,4,11,90,24,10,11,92,10]
n = len(arr)
for k in range(n):
    for i in range((n-k)-1):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
print(arr)
