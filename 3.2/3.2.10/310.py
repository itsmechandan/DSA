def LinearSearch(nums,a):
    n=len(nums)
    for i in range(n):
        if nums[i] == a:
            return True
    return False
def Longest_consecutive_sequence_bf(nums):
    n= len(nums)
    Longest = 1

    for i in range(n):
        x=nums[i]
        cnt=1
        while LinearSearch(nums,x+1):
            x=x+1
            cnt=cnt+1
        Longest = max(Longest,cnt)
    return Longest

def better(nums):
    n=len(nums)
    sorted_nums = sorted(nums)
    cnt = 1
    Longest = 1
    for i in range(n-1):
        if sorted_nums[i+1]-sorted_nums[i]==1:
            cnt = cnt+1
        Longest = max(Longest,cnt)
    return Longest

arr=[3, 8, 5, 7, 6]
print(f"Brute force: {Longest_consecutive_sequence_bf(arr)}")
print(f"better: {better(arr)}")