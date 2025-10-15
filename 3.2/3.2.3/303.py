# Moore's voting Algorithm
def majorityelementrepeating(arr):
    n=len(arr)
    count=0
    element=0
    for i in range(n):
        if count == 0:
            count =1
            element = arr[i]
        elif element == arr[i]:
            count +=1
        else:
            count -=1
    for i in range(n):
        if arr[i]==element:
            count +=1
        if count > n/2:
            return element
    return -1
arr=[7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]
print(f"majority element repeating greater than n/2 times is: {majorityelementrepeating(arr)}")