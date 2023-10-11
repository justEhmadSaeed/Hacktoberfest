# Selection Sort Algorithm
# function to perform selection sort
def selectionSort(arr,n):
    for i in range(0,n-1):
        min = i
        for j in range(i+1,n):
            # find element which is smaller than a[i] in right side of a[i] and swap it
            if arr[j]<arr[min]:
                min = j
        (arr[i],arr[min])=(arr[min],arr[i])


arr = [3, 4, 1, 5, 2]
print("Unsorted Array")
print(arr) # print unsorted array

n = len(arr)
selectionSort(arr,n)

# print sorted arry
print('Sorted Array in Ascending Order:')
print(arr)