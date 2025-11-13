def find_union_brute_force(arr1, arr2):
    """
    Finds the union of two sorted arrays using a set (brute-force approach).

    Args:
        arr1 (list): The first sorted array.
        arr2 (list): The second sorted array.

    Returns:
        list: The union of the two arrays, sorted and with duplicates removed.
    """
    # 1. Initialize a Set to store distinct elements
    # Sets in Python are highly efficient for adding and checking membership (O(1) average time).
    union_set = set()

    # 2. Traverse arr1 and insert all elements into the set
    for element in arr1:
        union_set.add(element)

    # 3. Traverse arr2 and insert all elements into the set
    # The set automatically handles duplicates, ensuring only distinct elements remain.
    for element in arr2:
        union_set.add(element)

    # 4. Convert the set to a list and sort it
    # Since the input arrays were sorted, we only need to sort the final set elements.
    union_list = list(union_set)
    union_list.sort()

    return union_list

# Example Usage:
arr_a = [1,1, 2, 3, 4, 5]
arr_b = [1, 2, 4, 6, 7]
result = find_union_brute_force(arr_a, arr_b)

print("Array 1:", arr_a)
print("Array 2:", arr_b)
print("Union (Brute Force):", result)
# Expected Output: [1, 2, 3, 4, 5, 6, 7]