# Hashing Process
def findsubarrayusinghashing(arr,k):
    n=len(arr)
    current_sum=0
    max_length=0
    prefix_sum={0:-1}
    for i in range(n):
        current_sum +=arr[i]
        req_sum = current_sum-k
        if req_sum in prefix_sum:
            j = prefix_sum[req_sum]
            current_length = i-j
            max_length=max(current_length,max_length)
        if current_sum not in prefix_sum:
            prefix_sum[current_sum]=i
    return max_length

arr=[1,2,3,1,1,1,4,2,3]
k=3
print(findsubarrayusinghashing(arr,k))
            
