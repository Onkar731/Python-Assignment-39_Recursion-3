"""
Write a recursive function to calculate sum of first N odd natural numbers 
"""

# defining a function "sum_first_odd_naturals()" which takes a number as an argument
# and returns the sum of first N natural numbers
def sum_first_odd_naturals(num):
    if num == 1:
        return 1
    else:
        return num*2-1 + sum_first_odd_naturals(num-1)
    

# taking input from the user
num = int(input("Enter a number : "))

# printing sum_first_odd_naturals()
print("Sum of odd natural numbers :", sum_first_odd_naturals(num))