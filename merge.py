
def merge(arr, l , q, r):
    n1 = q-l +1 
    n2 = r-q
    L = [0]*(n1+1)
    R = [0]*(n2+1) 
    L[0:n1] = arr[l:q+1]
    R[0:n2] = arr[q+1:r+1]
    L[-1] =  float('inf') 
    R[-1] =  float('inf') 
    i = 0
    j = 0
    for k in range(l, r+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+= 1 
        else:
            arr[k] = R[j]
            j+=1 
    
def mergeSort(array, l, r):
    if l<r: 
        q = (l+r)//2
        mergeSort(array, l, q)
        mergeSort(array, q+1, r)
        merge(array, l, q, r )




def main():

    array= [1,5,6,9,7,5,1,65,6,41,45]
    array = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6,11]
    arr = array.copy()
    print(array)
    mergeSort(array, 0, len(array)-1)
    print(array)
    array = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6,11]
    print(sorted(array))
    print(arr)

if __name__== "__main__":
    main()