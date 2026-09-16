def RandomizedPartition(A, p, r):
    import random
    pivot = random.randint(p, r)
    A[pivot], A[r] = A[r], A[pivot]
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def RandomizedQuicksort(A, low, high, index):
    index += 1
    print ("Recursion index:", index, "Size:", high - low + 1, "Array:", A[low:high + 1])
    if low < high:
        pivot = RandomizedPartition(A, low, high)
        A = RandomizedQuicksort(A, low, pivot - 1, index)
        A = RandomizedQuicksort(A, pivot + 1, high, index)
    return A


A = [5,6,2,1,9,11,7,10,4]
print(RandomizedQuicksort(A, 0, len(A) - 1, 0))
