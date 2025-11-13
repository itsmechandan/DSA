def stockbuy(arr):
    n=len(arr)
    min = float('inf')
    max = float('-inf')
    for i in range(n):
        if arr[i]<min:
            min = arr[i]
            start = i
    for i in range(start,n):
        if arr[i]>max:
            max = arr[i]
    return max-min

arr=[7,1,5,3,6,4]
print(f" maxium profit: {stockbuy(arr)}")
