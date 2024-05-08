# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 23:27:22 2024

@author: ghosh
"""

arr=[64,34,25,5,22,11,90,12]
n=len(arr)

for i in range(n-1):
    minval_index=i
    for j in range(i+1,n):
        if arr[j]<arr[minval_index]:
            minval_index=j
    arr[i],arr[minval_index]=arr[minval_index],arr[i]
print(arr)
            