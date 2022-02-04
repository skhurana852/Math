arr = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(arr) + 1):
    for j in range(i+1, len(arr) + 1):
        print(arr[i:j])