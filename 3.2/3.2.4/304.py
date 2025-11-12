def bruteforce(arr):
    maxi= -200
    n=len(arr)
    for i in range(n):
        for j in range(i,n):
            sum=0
            for k in range(i,j):
                sum+=arr[k]
            maxi=max(sum,maxi)
    return maxi

def better(arr):
    maxi= -200
    n=len(arr)
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            maxi=max(sum,maxi)
    return maxi

def kadane_algorithm_standard(arr):
    # Check for empty array
    if not arr:
        return 0

    # Initialize both variables to the first element to correctly handle
    # arrays with only negative numbers.
    max_so_far = arr[0] 
    current_max = arr[0]

    # Iterate from the second element
    for i in range(1, len(arr)):
        # Calculate the maximum sum ending at the current position:
        # It's either the current element OR the current element plus the previous current_max.
        current_max = max(arr[i], current_max + arr[i])
        
        # Update the overall maximum sum found so far
        max_so_far = max(max_so_far, current_max)

    return max_so_far

# Im not so sure if this is kadane's algortihm

def proper_kadane(arr):
    maxi = -2000
    sum = 0
    n = len(arr)
    for i in range(n):
        sum += arr[i]
        maxi = max(sum,maxi)
        if sum < 0:
            sum = 0
    return maxi



    


            



arr=[-2,-3,4,-1,-2,1,5,-3]
print(f"brute force approach : {bruteforce(arr)} where time complexity is : O(n^3) and space complexity is O(1)")
print(f"better approach : {better(arr)} where time complexity is : O(n^2) and space complexity is O(1)")
print(f"Kadane's algorith approach : {proper_kadane(arr)} where time complexity is : O(n) and space complexity is O(1)")
