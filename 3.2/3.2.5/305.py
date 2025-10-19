def kadane_return_subarray(arr):
    n=len(arr)
    sum=0
    arrStart=-1
    arrEnd=-1
    maxi =0
    for i in range(n):
        if sum==0:
            start=i
        sum = sum+arr[i]
        if sum > maxi:
            maxi = sum
            arrStart = start
            arrEnd = i
        if sum < 0:
            sum = 0
    for i in range (arrStart,arrEnd+1):
        print(arr[i])


arr=[-2,-3,4,-1,-2,1,5,-3]
print(f"subarray: {kadane_return_subarray(arr)}")