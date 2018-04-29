# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 10:02:17 2018

@author: JIANG
"""
#时间复杂度 O(n+k)
def counting_sort(A,B,k):
    C=[0]*(100)#create a empty list
    for i in range(len(A)):
        C[A[i]]=C[A[i]]+1
    for i in range(1,k+1):
        C[i]=C[i]+C[i-1]
    for j in range(len(A)-1,-1,-1):
        B[C[A[j]]-1]=A[j]#需要减一 否则最大值无法保存
        C[A[j]]=C[A[j]]-1
    return B
        
arr = [4, 7, 8, 9,16,17, 1, 5]
k=max(arr)-min(arr)+1
m=max(arr)
n = len(arr)
B=[0]*(n+1)
B=counting_sort(arr,B,k)
#quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %B[i]),

'''
def countSort(arr):

    # The output character array that will have sorted arr
    output = [0 for i in range(256)]

    # Create a count array to store count of inidividul
    # characters and initialize count array as 0
    count = [0 for i in range(256)]

    # For storing the resulting answer since the 
    # string is immutable
    ans = ["" for _ in arr]

    # Store count of each character
    for i in arr:
        count[ord(i)] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(256):
        count[i] += count[i-1]

    # Build the output character array
    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1

    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans 

# Driver program to test above function
arr = "geeksforgeeks"
ans = countSort(arr)

def mandelbrot( h,w, maxit=20 ):
... """Returns an image of the Mandelbrot fractal of size (h,w)."""
... y,x = np.ogrid[ -1.4:1.4:h * 1j, -2:0.8:w * 1j ]
... c = x+y * 1j
... z = c
... divtime = maxit + np.zeros(z.shape, dtype=int)
...
... for i in range(maxit):
... z = z ** 2 + c
... diverge = z * np.conj(z) > 2 ** 2 # who is diverging
... div_now = diverge & (divtime==maxit) # who is diverging now
... divtime[div_now] = i # note when
... z[diverge] = 2 # avoid diverging too much
...
... return divtime

'''