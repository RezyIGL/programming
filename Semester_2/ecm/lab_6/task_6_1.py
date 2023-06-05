def merge(A: list, left: int, mid: int, right: int) -> list:
    # вспомогательный массив, в который будут сливаться элементы
    AUX = []

    # список, в который мы будем записывать порядок сливания элементов
    indexes = []

    # Инициализируем указатели i и j
    i = left
    j = mid + 1

    # Цикл, осуществляющий слияние
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            AUX.append(A[i])
            indexes.append(i)
            i += 1
        
        else:
            AUX.append(A[j])
            indexes.append(j)
            j += 1

    # Дописываем хвост (почитайте справку к функции extend для списков) и не забываем про indexes
    if i >= mid:
        AUX.extend(A[j:right + 1])
        indexes.extend([num for num in range(j, right + 1)])

    if j >= right:
        AUX.extend(A[i:mid + 1])
        indexes.extend([num for num in range(i, mid + 1)])

    # Возвращаем назад в массив A результат нашей работы (обратите внимание на присваивание срезу!)
    A[left:right + 1] = AUX

    print(*A)
    return indexes

# читаем массив A, массив B, склеиваем их
if __name__ == "__main__":
    arrA = list(map(int, input().split()))
    arrB = list(map(int, input().split()))
    newArr = arrA + arrB
    len_arr_A = len(arrA)
    # вызываем merge, результат преобразуем к нужному виду и выводим
    print(*merge(newArr, 0, len_arr_A-1, len(newArr)-1))
