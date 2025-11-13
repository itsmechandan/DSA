def findlargestelement(arr):
    n=len(arr)
    max=0
    for i in range(n):
        if(arr[i]>max):
            max=arr[i]
    return max
arr=[1,22,2421,2]
print(findlargestelement(arr))

# Another way to deal with this is sort the array and then print the last element of the array