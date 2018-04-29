# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 08:58:28 2018

@author: JIANG
"""
def partition(arr,low,high):
    i=low-1
    k=arr[high]
    for j in range(low,high):
        if arr[j]<k:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 #尾递归技术
def tail_recursice_quickSort(arr,low,high):
      while low<high:
         q=partition(arr,low,high)
         if q<(high-low)/2:
             tail_recursice_quickSort(arr,low,q-1)
             low=q+1
         else:
             tail_recursice_quickSort(arr,q+1,high)
             high=q-1

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
tail_recursice_quickSort(arr,0,n-1)
#quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),
 
# This code is contributed by Mohit Kumra
