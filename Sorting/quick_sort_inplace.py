# -*- coding: utf-8 -*-

def quick_sort_inplace(A, l, r):
    """ Sort the list from A[l] to A[r-1] inclusive using the quick-sort algorithm.”””"""
    global counter
    if r - l < 2:
        return
    counter += r - l - 1
    #lengths.append(r-l-1)
    # Choose the pivot to be the left, right or the "middle" element
    #pi = l
    #pi = r - 1
    pi = choose_middle(A, l, r-1, l + (r-l)//2 + (r-l)%2 - 1 )
    p = A[pi]
    # use print only for small lengths of A
    #print('Partitioning', A[l:r] ,'around pivot {} with index {}'.format(p, pi))
    
    A[pi], A[l] = A[l], A[pi]
    j = l + 1
    for k in range(l+1, r):
        if A[k] < p:
            A[k], A[j] = A[j], A[k]
            j += 1
    A[l], A[j-1] = A[j-1], A[l]
    
    quick_sort_inplace(A, l, j-1)
    quick_sort_inplace(A, j, r)
    

def choose_middle(A, p1, p2, p3):
    return sorted([ [A[p1],p1], [A[p2],p2], [A[p3],p3] ])[1][1]

# Test
if __name__ == '__main__':
    
    counter = 0
    #lengths = []
    print("Test")
    a = [9, 3, 8, 2, 5, 1, 4, 7,-2, 6, 12, 13, -4, 0, -2, 9]
    print('original:', a)
    quick_sort_inplace(a, 0, len(a))
    print('sorted:', a)
    print("Number of comparisons: ", counter, end = "\n")


    ### Read the array from a text file
    fname = "./QSinput100000.txt"
    with open(fname, 'r') as f:
        content = f.readlines()
    input_array = [int(x) for x in content]

    counter = 0
    #lengths = []
    quick_sort_inplace( input_array, 0, len(input_array) )

    print(input_array == list( range(1, len(input_array)+1 ) ) )
    #print(input_array)
    #print(sum(lengths), max(lengths), min(lengths))
    #print(lengths)
    print("Number of comparisons: ", counter)