def partition(arr, q, r):
    x = arr[r]
    i = q -1
    for j in range(q,r):
        if arr[j] <= x:
            i +=1 
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def quick_sort(arr, l, r ):
    if(l < r):
        q = partition(arr, l, r)
        print(arr)
        quick_sort(arr, l, q-1)
        quick_sort(arr, q+1, r)

def main():

    array= [1,5,6,9,7,5,1,65,6,41,45]
    array = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6,11]
    print(array)
    quick_sort(array, 0, len(array)-1)
    print(array)

if __name__== "__main__":
    main()