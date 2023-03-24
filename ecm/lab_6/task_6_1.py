def merge(A, left, mid, right):
    AUX = []
    indexes = []

    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            AUX.append (A[i])
            indexes.append (i)
            i += 1
        else:
            AUX.append (A[j])
            indexes.append (j)
            j += 1

    if i < mid + 1:
        AUX.extend (A[i : mid + 1])
        indexes.extend ([ _ for _ in range (i, mid + 1)])
    elif j < right + 1:
        AUX.extend (A[j :  right + 1])
        indexes.extend ([ _ for _ in range (j, right + 1)])
    A[left:right+1] = AUX

    return AUX, indexes

def merge_start(arr1: list, arr2: list) -> tuple:
    lenArr1 = len(arr1)
    lenArr2 = len(arr2)
    length = lenArr1 + lenArr2
    array = arr1 + arr2
    return merge(array, 0, lenArr1 - 1, length - 1)

if __name__ == "__main__":
    result = merge_start(list(map(int, input().split())), list(map(int, input().split())))
    print(*result[0])
    print(*result[1])