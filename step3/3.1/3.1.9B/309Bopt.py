def intersection(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    i=0
    j=0
    inte = list()
    while i<n and j<m:
        if(arr1[i]<arr2[j]):
            i=i+1
        if(arr1[i]>arr2[j]):
            j=j+1
        else:
            inte.append(arr1[i])
            i=i+1
            j=j+1
    return inte

arr1 = [1,2,2,3,3,4,5,6]
arr2=[2,3,3,5,6,6,7]
print(intersection(arr1,arr2))