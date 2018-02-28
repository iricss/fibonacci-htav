# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 09:11:45 2018

@author: Hosna
"""

""" n = int(input ("please enter a number:"))"""

def fib_loop(n):
    
    Pre_Fib_value = 0
    Pre2_Fib_value = 1
    Fib_value = 1

    for i in range(n):
    
         Fib_value = Pre_Fib_value + Pre2_Fib_value
         Pre2_Fib_value = Pre_Fib_value
         Pre_Fib_value = Fib_value
         print(Fib_value)
    
    