"""
Write a recursive function to calculate sum of cubes of first N natural numbers
"""

# defining a function "sum_cubes_first_naturals()" which takes a number
# as an argument and returns the sum of cubes of first N natural numbers
def sum_cubes_first_naturals(num):
    if num == 1:
        return 1
    else:
        return num**3 + sum_cubes_first_naturals(num-1)
    

# taking input from the user
num = int(input("Enter a number : "))

# calling sum_cubes_first_naturals()
print("Sum of cubes of first %d natural numbers is : " %(num), sum_cubes_first_naturals(num))