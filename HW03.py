# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 02:53:32 2021

@author: star5
"""

import random

ans = random.randint(1,100)

guess = 0
top = 100
bot = 1
count = 0

while ans != guess:
    print('輸入',bot,'-',top,'之間的整數:')
    guess = int(input())
    count +=1
    if ans == guess:
        print('猜對了')
    elif count == 5 :
        print('已猜錯5次')
        break
    if guess > ans :
        print('猜小一點')
        top = guess-1
    if guess < ans :
        print('猜大一點')
        bot = guess + 1