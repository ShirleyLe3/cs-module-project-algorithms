'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    result, zeroes = [], []
    for num in arr:
        if num != 0:
            result.append(num)
        else:
            zeroes.append(num)
    result += zeroes
    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")