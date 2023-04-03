# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 19:51:09 2020

@author: User
"""
#IF CONTINUE after continue tHat iterations won't be executed.will come to next loop.
#if BREAK after break the loops will exit.won't going to execute the remaings
#IF PASS
cart=[100,20,5,200,600,800,25,15]
for items in cart:
    if items<=500:
        print("checked",items)
        continue
    print("this is below 500 cart")
   
print("hai")
