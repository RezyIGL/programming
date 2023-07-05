def func(arr):
    arrLen = len(arr)
    if arrLen == 0:
        return 0

    return 1 + func(arr[1:])

if __name__ == "__main__":
    myArray = [1, 2, 3, 4, 5]
    print(func(myArray))