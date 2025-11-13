def longestsubarraybruteforce(arr,k):
    n=len(arr)
    legnth = 0
    max_legnth=0
    for i in range(n-1):
        sum=arr[i]
        if sum==k:
            legnth = 1
        for j in range(i+1,n):
            if sum + arr[j]<k:
                sum = sum+arr[j]
            if sum + arr[j] == k:
                legnth = j-i+1
                break
            if sum + arr[j] > k:
                break
        if legnth > max_legnth:
            max_legnth = legnth
    return max_legnth
arr=[2,3,5,1,9]
k=10
print(longestsubarraybruteforce(arr,k))
