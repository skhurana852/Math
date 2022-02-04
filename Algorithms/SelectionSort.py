arr = [64, 25, 12, 22, 11]
idx =0 
for i in range(len(arr)):
    min = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min]:
            min = j
    temp = arr[i]
    arr[i] = arr[min]
    arr[min] = temp
    print(arr)

print(arr)