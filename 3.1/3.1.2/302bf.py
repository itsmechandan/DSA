def findsecondlargest(arr):
    sorted_array = sorted(arr)
    n = len(sorted_array)
    
    largest = sorted_array[-1]
    
    for i in range(n - 2, -1, -1):
        if sorted_array[i] < largest:
            return sorted_array[i]
    return -1

arr = [1, 2, 4, 7, 7, 5]
print(f"Second Largest (Sorting Method): {findsecondlargest(arr)}")
