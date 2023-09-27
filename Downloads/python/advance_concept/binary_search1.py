def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # Element not found

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid  # Element found at index 'mid'
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Example usage:
arr = [5, 13, 15, 24, 30, 38, 40, 45]
target = 13
result = binary_search_recursive(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list.")
