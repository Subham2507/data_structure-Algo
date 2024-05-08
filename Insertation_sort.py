# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 23:40:56 2024

@author: ghosh
"""

arr=[6,5,4,3,2,1]
n=len(arr)

for i in range(1,n):
    j=i
    while(j>0 and arr[j-1]>arr[j]):
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j=j-1
print(arr)