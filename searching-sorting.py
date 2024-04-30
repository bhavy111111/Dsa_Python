#Linear Search 
#Brute Force
#Positive - No need of sorted array
#Negative - Time complexity is O(n)
#More the number of array , searching time will also be doubled

def linear_search(arr , item):
    for i in range(len(arr)):
        if arr[i]==item:
            return i
    return -1
arr =[12,34,56,1,67,100]
print(linear_search(arr,100))

# Binary Searach
#It works only on sorted array

def binary_search(arr, low , high , item):
    print("low = ", low , 'High = ', high , end =' ')
    
    if low <= high:

        mid =(low + high)//2
        print('Midd value is ',arr[mid])
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            binary_search(arr,low , mid-1 , item)
        else:
            return binary_search(arr, mid+1 , high, item)
    else:
        return -1
    
arr=[12,24,35,46,57,68,80,99,100]
print(binary_search(arr,0,len(arr)-1,100))

#Binary Search - nlogn + logn
#If you are searching for k time w, if k is large then go for binary search

#Sorted algo

def is_sorted1(arr):

    flag_sorted=True

    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            flag_sorted = False
    return sorted

arr=[1,2,3,4,5,6]
print(is_sorted1(arr))

# Monkey Sort

import random
import time 
#a=[1,2,3,4]
#random.shuffle(a)
#print(a)

def mokey_sort(arr):
    while not is_sorted1(arr):
        time.sleep(1)
        random.shuffle(arr)
        print(arr)
    print(arr)

#Bubble Sort
# Total Elements - n 
# Swap - (n-1)

def bubble_sort(arr):
  
    for i in range(len(arr)-1):
        flag=0
        for j in range(len(arr)-1-i):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        if flag==0:
            print('Sorted ')
            break
    print(arr)

arr = [1,2,4,5,6]
print(bubble_sort(arr))

#Bubble Sort
#Worst Case n^2 - n-1 AP
#Sorted - Best Case - O(n)
#By nature Bubble Sort is not adaptive , But by using flag technique we can make it adaptive


#Selection Sort
