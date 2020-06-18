'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr): #o(n^2)
    for x in arr:
        if arr.count(x) == 1:
            return x

def single_number_optimized(nums): # O(n)
    counts = {}  # keep track of number of times an item occurs in input
    for num in nums:      # loop through input list O(n)
        if num in counts:
            del counts[num]
        else:
            # add item
            counts[num] = 1
    for k, v in counts.items(): # O(1)
        if v == 1:
            return k


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")