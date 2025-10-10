# move all zeroes to the end
def movezeroesbruteforce(arr):
    n = len(arr)
    temp = []
    for i in range(n):
        if arr[i]!= 0:
            temp.append(arr[i])
    m = len(temp)
    for i in range(m):
        arr[i] = temp[i]
    for i in range(m,n):
        arr[i] = 0

    return arr

my_array = [1,0, 2, 3,0,0, 4, 5, 6, 7]
print(f"Original Array: {my_array}")
rotated_array = movezeroesbruteforce(my_array)
print(f"Array after  moving zeroes (Brute Force): {rotated_array}")       



    