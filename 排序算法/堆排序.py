# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 08:11:38 2018

@author: JIANG
"""

class HeapSort():
    def max_heap(A,n,i):
        l=2*i+1
        r=2*i+2
        if l<n and A[l]>A[i]:
              largest=l
        else:
            largest=i
        if r<n and A[r]>A[largest]:
            largest=r
        else:
            largest=i
        if i!=largest:
            A[i],A[largest]=A[largest],A[i]
            max_heap(A,n-1,largest)
    def build_max_heap(A):
        A.heap_size=len(A)
        for i in range(len(A)/2,-1):
            max_heap(A,i)
    def heap_sort(A):
        build_max_heap(A)
        n=len(A)-1
        for i in range(len(A),-1):
            A[0],A[i]=A[i],A[0]
            max_heap(A,--n,0)

arr = [ 12, 11, 13, 5, 6, 7]
HeapSort.heap_sort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("%d" %arr[i]),
            
            
        