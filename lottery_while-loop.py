#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 13:19:58 2020

@author: jessedesimone
"""
#%%
from random import seed
from random import randint
a=[]
for i in range(100):
    ticketno=randint(100000,2000000)
    a.append(ticketno)
    print(ticketno)
#%%
value=input('enter your ticket number: ')

if int(value) in a:
    print('You have won the lottery!!!!')
    a.index(int(value))
else:
    print('Sorry, your number was not called')
    
#%%
while value != 'quit':
    value=input('enter your ticket number or quit to exit: ')
    if value != 'quit':
        value=int(value)
        if value in a:
            print('You have won the lottery!!!!')
            ind=a.index(value)
            print('your number was found at index location: ', ind)
        else:
            print('Sorry, your number was not called')
    if value == 'quit':
        print('Thanks for playing')
    
    
    
    
    
    