def find_union_optimal(arr1, arr2):
    """
    Finds the union of two sorted arrays using the Two-Pointer technique.

    Args:
        arr1 (list): The first sorted array (size n).
        arr2 (list): The second sorted array (size m).

    Returns:
        list: The union of the two arrays, sorted and with duplicates removed.
    """
    n, m = len(arr1), len(arr2)
    i, j = 0, 0  # Pointers for arr1 and arr2
    union_list = []

    while i < n and j < m:
        # Case 1: arr1[i] is smaller
        if arr1[i] <= arr2[j]:
            # Add arr1[i] if it's not already the last element added to the union
            if not union_list or union_list[-1] != arr1[i]:
                union_list.append(arr1[i])
            i += 1  # Move arr1 pointer forward

        # Case 2: arr2[j] is smaller
        else: # arr2[j] < arr1[i]
            # Add arr2[j] if it's not already the last element added to the union
            if not union_list or union_list[-1] != arr2[j]:
                union_list.append(arr2[j])
            j += 1  # Move arr2 pointer forward

    # Case 3: One array is exhausted, add the remaining elements from the other array
    
    # Add remaining elements of arr1 (if any)
    while i < n:
        if union_list[-1] != arr1[i]:
            union_list.append(arr1[i])
        i += 1

    # Add remaining elements of arr2 (if any)
    while j < m:
        if union_list[-1] != arr2[j]:
            union_list.append(arr2[j])
        j += 1

    return union_list

# Example Usage:
arr_a = [1, 2, 3, 4, 5]
arr_b = [1, 2, 4, 6, 7]
result_opt = find_union_optimal(arr_a, arr_b)

print("Union (Optimal):", result_opt)