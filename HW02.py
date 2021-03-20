# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

start = int(input("初始值:"))
end = int(input('終止值:'))

print('4的倍數有:',end = '')
for i in range(start,end+1):
    if i % 4 ==0 :
        print(i,end=',')
        
print()

print('1-',end,'的質數有:',end='')
for j in range(1,end):
    check = 0
    for a in range(2,j):
        if j % a == 0:
            check+=1
    if check == 0 and j != 1:
            print(j,end=',')
print('程式執行完畢')