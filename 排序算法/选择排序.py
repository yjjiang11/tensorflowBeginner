# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 09:30:46 2018

@author: JIANG
"""
#
def selection_sort2(arr):
   for i in range(0,len(arr)):
       key=i
       for j in range(1,len(arr)-i):
           if arr[j]<arr[key]:
              key=j
       arr[i],arr[key]=arr[key],arr[i]
arr = [64, 25, 12, 22, 11]
# Traverse through all array elements
def selection_sort(arr):
 for i in range(0,len(arr)):
     
    # Find the minimum element in remaining 
    # unsorted array
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
             
    # Swap the found minimum element with 
    # the first element        
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
selection_sort2(arr)
print ("Sorted array")
for i in range(len(arr)):
    print("%d" %arr[i]),