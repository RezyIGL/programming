def insertMas2Mas(A: list, n: int, i: int, B: list):
    # если вставлять уже некуда, пишем full
    if len(A) - n < len(B):
        print("full")
        return 

    # в цикле печатаем переносы элементов
    for k in range(n, i, -1):
        A[k + len(B) - 1] = A[k-1]
        print(f"A[{k + len(B) - 1}] = A[{k-1}]") 

    # в цикле печатаем копирование элементов из B в нужные места
    for k in range(i, i + len(B)):
        A[k] = B[k-i]
        print(f"A[{k}] = {A[k]}")

if __name__ == "__main__":
    n, i = (map(int, input().split()))
    arrA = list(map(int, input().split()))
    arrB = list(map(int, input().split()))
    insertMas2Mas(arrA, n, i, arrB)
    