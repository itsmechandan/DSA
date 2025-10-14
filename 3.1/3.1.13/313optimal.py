# This technique is called sliding window
def findsubarrayoptimal(arr,k):
    n=len(arr)
    summ=0
    length=0
    left=0
    max_len=0
    for right in range(n):
        summ +=arr[right]
        while ( summ>k):
            summ-=arr[left]
            left+=1
        if(summ==k):
            length =  right-left+1
            max_len=max(length,max_len)
    return max_len
arr=[1,2,3,1,1,1,1,3,3]
print(findsubarrayoptimal(arr,6))