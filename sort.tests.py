def Comb_sort(arr):
    n = len(arr)
    step = n

    while step > 1 or flag:
        if step > 1:
            step = int(step / 1.247331)
        flag, i = False, 0
        while i + step < n:
            if arr[i] > arr[i + step]:
                arr[i], arr[i + step] = arr[i + step], arr[i]
                flag = True
            i += step

a = [5, 4, 1, 3, 2]

print("Сортировка расческой")
Comb_sort(a)
print(a)

b = [5, 4, 1, 3, 2]

print("Метод sort")
b.sort()
print(b)


