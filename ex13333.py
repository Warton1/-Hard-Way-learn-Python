#Import necessary libraries
import pandas as pd
import numpy as np

# GRADED
# Provided below are functions that are completely defined (add_numbers),
# partially defined (sub_numbers) and not defined (mult_numbers)
# (a) Complete sub_numbers so that it return difference of two numbers
# (b) Write a function called mult_numbers to multiply two numbers

def add_numbers(n1, n2):
    result = n1 + n2
    return result

def sub_numbers(n1, n2):
    # Write code to return sum of a and b
    result =  n1-n2
    return result
print(mult_numbers(add_numbers(5,4), sub_numbers(5,4)))