# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 21:36:37 2024

@author: ghosh
"""

arr=[7,12,9,11,3]
n=len(arr)
count=0
for i in range(n-1):
    swapped=False
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapped=True
        count+=1
    if not swapped:
        break
print(arr)
print(count)