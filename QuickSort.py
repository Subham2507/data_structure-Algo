# -*- coding: utf-8 -*-
"""
Created on Mon May  6 23:24:58 2024

@author: ghosh
"""


def partition(A,l,h):
    pivot=A[l]
    i=l
    j=h
    while(i<j):
        while(A[i]<=pivot and i<=h-1):
            i+=1
        while(A[j]>pivot and j>=i):
            j-=1
        if(i<j):
            A[i],A[j]=A[j],A[i]
    A[l],A[j]=A[j],A[l]
    return j

def quick(A,l,h):
    if(l<h):
        j=partition(A, l, h)
        quick(A, l, j-1)
        quick(A, j+1, h)
        

A=[10,16,8,12,15,6,3,9,5]
quick(A, 0, len(A)-1)
print(A)