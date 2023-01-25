"""
Write a recursive function to calculate sum of first N even natural numbers 
"""

# defining a function "sum_first_even_naturals()" which takes a number as an argument
# and returns the sum of first N natural numbers
def sum_first_even_naturals(num):
    if num == 1:
        return 2
    else:
        return num*2 + sum_first_even_naturals(num-1)
    

# taking input from the user
num = int(input("Enter a number : "))

# printing sum_first_even_naturals()
print("Sum of enve natural numbers :", sum_first_even_naturals(num))