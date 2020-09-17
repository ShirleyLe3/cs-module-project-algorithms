'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    setA, setB = set(), set()
    for num in arr:
        if num not in setA:
            setA.add(num)
        else:
            setB.add(num)
    (single,) = set.difference(setA, setB)
    return single

# def single_number(arr):
#     s = set()
#     for num in arr:
#         if num in s:
#             s.remove(num)
#         else:
#             s.add(num)
#     (single,) = s
#     return single

# def single_number(arr):
#     for num in arr:
#         if arr.count(num) == 1:
#             return num

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")