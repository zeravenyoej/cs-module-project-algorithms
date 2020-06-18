'''
Input: an integer
Returns: an integer
''' 

def eating_cookies(n):
    eaten = 0      # number of cookies eaten
    if eaten > n:  # base case - if cookes eaten is more than the total number of cookies
        return 0
    elif eaten == n: # If eaten is the number of available cookies, return a count of 1
        return 1
    else:     # call function again to loop through each potential options incrementing eaten by potential options
        return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

