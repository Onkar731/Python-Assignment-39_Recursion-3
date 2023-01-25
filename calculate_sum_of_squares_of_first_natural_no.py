"""
Write a recursive function to calculate sum of squares of first N natural numbers
"""

# defining a function "sum_squares_first_naturals()" which takes a number
# as an argument and returns the sum of squares of first N natural numbers
def sum_squares_first_naturals(num):
    if num == 1:
        return 1
    else:
        return num**2 + sum_squares_first_naturals(num-1)
    

# taking input from the user
num = int(input("Enter a number : "))

# calling sum_squares_first_naturals()
print("Sum of squares of first %d natural numbers is : " %(num), sum_squares_first_naturals(num))