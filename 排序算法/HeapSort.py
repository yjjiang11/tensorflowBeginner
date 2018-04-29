# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 08:29:06 2018

@author: JIANG
"""

def heapify(arr, n, i):
    largest=i
    l=2*i+1
    r=2*i+2
    if r<n and arr[r]>arr[largest]:
        largest=r
    else:
        largest=i
    if l<n and arr[l]>arr[largest]:
        largest=l
    if largest!=i:
       arr[i],arr[largest]=arr[largest],arr[i]
       heapify(arr,n,largest)
       
 
# The main function to sort an array of given size
def heapSort(arr):
    n=len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]

        heapify(arr,i,0)
def heapSort2(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)
 
 
# Driver code to test above
arr = [ 12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n-1):
    print ("%d" %arr[i]),
# This code is contributed by Mohit Kumra