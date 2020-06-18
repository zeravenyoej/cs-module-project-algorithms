'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr): #O(n)
    num = arr.count(0)
    while num != 0: 
        arr.append(arr.pop(arr.index(0)))
        num -=1
    return arr

'''
what if we had a pointer that started at the beginning
and a pointer that started at the end
and they moved towards each other in the middle?
​
if the left pointer "sees" a zero and the right pointer "sees" a non-zero
swap
​
if the left sees a non-zero increment
if the right sees a zero increment
'''

# def moving_zeroes(arr):
#     # left pointer at the beginning
#     left = 0
#     # right pointer at the end
#     right = len(arr)-1
#     # loop until left and right pointers meet or right pointer passes the left pointer
#     while left > right:
#         # swap situation:
#         # left sees zero and right sees non-zero
#         if arr[left] == 0 and arr[right] != 0:
#             # swap the items
#             arr[left], arr[right] = arr[right], arr[left]
#             # increment left
#             left +=1
#             # decrement right
#             right -=1
#         # non-swap situation
#         else:
#             # if left sees non-zero
#             if arr[left] != 0:
#                 # increment left
#                 left +=1
#             # if right sees zero
#             if arr[right] == 0:
#                 # decrement right
#                 right -=1
#     return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")