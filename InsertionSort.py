def InsertionSort(A, n, comp, exch):
    i = 1
    for i in range(n):
        key = A[i]
        j = i - 1
        comp += 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1
            exch += 1
        A[j + 1] = key
    return(A, comp, exch)

A = [1,2,3,4,5,6,7,8,9,10]
B = [10,9,8,7,6,5,4,3,2,1]
print(InsertionSort(A, len(A), 0, 0))
print(InsertionSort(B, len(B), 0, 0))
