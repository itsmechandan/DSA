# Brute force
def leftRotate_bruteForce(arr, d):
    """
    Left-rotates an array (list) by 'd' steps using the brute-force approach.

    Args:
        arr (list): The array to be rotated.
        d (int): The number of steps to rotate left.
    """
    n = len(arr)

    # Handle cases where d is greater than n or d is negative
    d = d % n
    if d == 0:
        return arr

    # 1. Store the first 'd' elements in a temporary list (temp)
    # Equivalent to: for(i = 0; i < d; i++){ temp[] = arr[i] }
    temp = []
    for i in range(d):
        temp.append(arr[i])

    # 2. Shift the remaining (n-d) elements to the front
    # Equivalent to: for(i = d; i < n; i++){ arr[i-d] = arr[i] }
    for i in range(d, n):
        arr[i - d] = arr[i]

    # 3. Copy the elements from 'temp' back to the end of 'arr'
    # Equivalent to: for(i = n-d; i < n; i++){ arr[i] = temp[i - (n-d)] }
    # The index for 'temp' is: i - (n - d)
    temp_index = 0
    for i in range(n - d, n):
        arr[i] = temp[temp_index]
        temp_index += 1

    return arr

# --- Example Usage ---
my_array = [1, 2, 3, 4, 5, 6, 7]
steps = 3
print(f"Original Array: {my_array}")
rotated_array = leftRotate_bruteForce(my_array, steps)
print(f"Array after {steps} left rotations (Brute Force): {rotated_array}")