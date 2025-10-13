def moveZeroesOptimal(arr):
    n = len(arr)

    # 1. Find the index (j) of the first '0'
    j = -1
    for i in range(n):
        if arr[i] == 0:
            # FIX: Use assignment (=) instead of comparison (==)
            j = i
            break

    # If no '0' is found, the array is already correct, so return
    if j == -1:
        return arr

    # 2. Use a second pointer (i) to iterate from the element after the first '0' (j+1)
    #    and swap non-zero elements with the element at index 'j'.
    for i in range(j + 1, n):
        if arr[i] != 0:
            # Swap arr[i] (non-zero) with arr[j] (zero)
            # This is the Pythonic way to swap elements
            arr[i], arr[j] = arr[j], arr[i]

            # Move 'j' to the next zero position (which is now at j+1)
            j = j + 1

    return arr

# --- Example Usage ---
my_array = [0, 1, 0, 3, 12]
print(f"Original Array: {my_array}")
moveZeroesOptimal(my_array)
print(f"Array after moving zeroes: {my_array}")

my_array_2 = [1, 2, 3, 4, 5]
print(f"Original Array: {my_array_2}")
moveZeroesOptimal(my_array_2)
print(f"Array after moving zeroes: {my_array_2}")