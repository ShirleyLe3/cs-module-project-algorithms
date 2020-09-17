"""
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
"""

# def sliding_window_max(nums, k):
#     result = []
#     for i, num in enumerate(nums):
#         result.append(max(nums[i : i + k]))
#         if i + k >= len(nums):
#             break
#     return result

def sliding_window_max(nums, k):
    result = []
    maximum = max(nums[:k])
    max_count = 0
    for i, num in enumerate(nums):
        max_count -= 1
        if max_count <= 0:
            maximum = num
            for j, num in enumerate(nums[i : i + k]):
                if num >= maximum:
                    maximum = num
                    max_count = j + 1
        elif nums[i + k - 1] > maximum:
            maximum = nums[i + k - 1]
            max_count = k
        result.append(maximum)
        if i + k >= len(nums):
            break
    return result


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
