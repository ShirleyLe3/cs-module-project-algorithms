"""
Input: an integer
Returns: an integer
"""

def eating_cookies(n):
    total = 0
    count = [1, 1, 2]
    if n < 3:
        return count[n]
    for i in range(n - 2):
        total = sum(count)
        count.pop(0)
        count.append(total)
    return total


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies"
    )
