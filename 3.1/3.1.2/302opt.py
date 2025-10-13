def findsecondlargest_optimal(arr):
    if len(arr) < 2:
        return -1 # Cannot find second largest
        
    # Initialize largest and second_largest to minimum possible values
    # Or, preferably, handle the first two elements.
    # Using float('-inf') ensures it works with positive and negative numbers.
    largest = float('-inf')
    second_largest = float('-inf')
    
    for element in arr:
        if element > largest:
            # Current element is the new largest
            second_largest = largest # Old largest becomes second largest
            largest = element
        elif element < largest and element > second_largest:
            # Current element is smaller than the largest, 
            # but larger than the current second largest
            second_largest = element
            
    # Check if a second largest was actually found (i.e., not still float('-inf'))
    if second_largest == float('-inf'):
        return -1
    else:
        return second_largest

arr = [1, 2, 4, 7, 7, 5]
print(f"Second Largest (Optimal O(n) Method): {findsecondlargest_optimal(arr)}")