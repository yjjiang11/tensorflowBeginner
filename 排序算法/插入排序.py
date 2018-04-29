# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 09:06:48 2018

@author: JIANG
"""

def insert_sort(arr):
    for i in range(0,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
arr = [12, 11, 13, 5, 6]
insert_sort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])