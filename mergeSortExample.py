# mergeSort in python 3
# Pu Jiao

def merge(arr,start,m,end):
    left=arr[start:m]
    right=arr[m+1:end]
    i,j,k=0,0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[i]
        j+=1
        k+=1


def mergeSort(arr,start,end):
    if start < end:
        m=(end+start)//2
        mergeSort(arr,start,m)
        mergeSort(arr,m+1,end)
        merge(arr,start,m,end)




# Driver code to test above 
arr = [12, 11, 13, 5, 6, 7] 
n = len(arr) 
print ("Given array is") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
mergeSort(arr,0,n-1) 
print ("\n\nSorted array is") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
# This code is contributed by Mohit Kumra 

