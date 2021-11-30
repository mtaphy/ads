def mergeSort(arr):
    '''
        Python implementation of merge sort.
    '''
    if len(arr) > 1:
        # find the middle point of the array
        m = len(arr) // 2

        # devide array into two halves: Left, Right
        L = arr[:m]
        R = arr[m:]

        # sorting left half
        mergeSort(L)
        # sorting right half
        mergeSort(R)

        # merge
        l = r = k = 0

        while l < len(L) and r < len(R):
            if L[l] < R[r]:
                arr[k] = L[l]
                l += 1
            else:
                arr[k] = R[r]
                r += 1
            k += 1

        # add elements left in L
        while l < len(L):
            arr[k] = L[l]
            l += 1
            k += 1

        # add elements left in R
        while r < len(R):
            arr[k] = R[r]
            r += 1
            k += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")
    print()


if __name__ == '__main__':
    arr = [4, -2, -7, 10, 0, 2, 5, 4, 2, 1]
    print("Given array is:", end = "\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is:", end = '\n')
    printList(arr)
