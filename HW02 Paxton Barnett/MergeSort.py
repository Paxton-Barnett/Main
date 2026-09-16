def Merge(A, p, q, r):
    left = len(A[p:q + 1])
    right = len(A[q + 1:r + 1])
    L = A[0:left]
    R = A[0:right]
    i = 0
    for i in range(0, left):
        L[i] = A[p + i]
    j = 0
    for j in range(0, right):
        R[j] = A[q + 1 + j]
    i = 0
    j = 0
    k = p
    while i < left and j < right:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < left:
        A[k] = L[i]
        i += 1
        k += 1
    while j < right:
        A[k] = R[j]
        j += 1
        k += 1
    return A

def MergeSort(A, p, r, index):
    index += 1
    print ("Recursion index:", index, "Size:", r - p + 1, "Array:", A[p:r + 1])
    if p >= r:
        return A
    q = (p + r) // 2
    A = MergeSort(A, p, q, index)
    A = MergeSort(A, q + 1, r, index)
    A = Merge(A, p, q, r)
    return A

A = [8,3,7,5,9,2]
print(MergeSort(A, 0, len(A) - 1, 0))