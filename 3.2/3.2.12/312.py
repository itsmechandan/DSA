def bruteforce(arr):
    n = len(arr)
    m = len(arr[0])
    arr2 = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            arr2[j][n-1-i] = arr[i][j]
    return arr2

def optimal(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]

    for i in range(n):
        arr[i].reverse()

    return arr

arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

arr2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(f"brute: {bruteforce(arr)}")
print(f"optimal: {optimal(arr2)}")