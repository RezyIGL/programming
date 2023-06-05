def insert2Mas(A: list, n: int, i: int, elem: int):
    # если вставлять уже некуда, пишем full
    if len(A[n:]) == 0:
        print("full")

    # в цикле печатаем переносы элементов
    for k in range(n, i, -1):
        A[k] = A[k-1]
        print(f'A[{k}] = A[{k-1}]')
    A[i] = elem
    
    # печатаем копирование элемента elem в нужное место
    print(f'A[{i}] = {elem}')
    
if __name__ == "__main__":
    n, i, elem = (map(int, input().split()))
    arrA = list(map(int, input().split()))
    insert2Mas(arrA, n, i, elem)