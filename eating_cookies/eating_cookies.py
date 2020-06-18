'''
Input: an integer
Returns: an integer
''' 

# def eating_cookies(n):
#     eaten = 0      # number of cookies eaten
#     if eaten > n:  # base case - if cookes eaten is more than the total number of cookies
#         return 0
#     elif eaten == n: # If eaten is the number of available cookies, return a count of 1
#         return 1
#     else:     # call function again to loop through each potential options incrementing eaten by potential options
#         return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)




def eating_cookies(n, cache=None):
    if n < 0:      # check for negative values
        return 0  # getting to a negative number mean we didn't find one of the ways
    if n == 0:      # base case: when there are no more cookies
        return 1  # getting to 0, means we found a way to eat our cookies
    
    if cache is None:   #if no cache yet, create one
        cache = {}
    
    if n in cache:      # check for previously computed answer in our cache
        return cache[n]
    
    # this represents our recursive case # three possible decisions: eat 1 cookie, 2 cookies, or 3 cookies
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

