<<<<<<< HEAD
import math
from random import randrange


=======
>>>>>>> cb2aa518baad3e508ddebe40a0d9c8566c7818ce
def insertion(li: object) -> object:
    for i in range(1, len(li)):
        j = i - 1
        x = li[i]
        while j >= 0 and li[j] > x:
            li[j + 1] = li[j]
            j = j - 1
        li[j + 1] = x
    return li

<<<<<<< HEAD

def insertion_reverse(li: object) -> object:
    for i in range(len(li) - 1, 0, -1):
=======
def insertion_reverse(li: object) -> object:
    for i in range(len(li)-1, 0, -1):
>>>>>>> cb2aa518baad3e508ddebe40a0d9c8566c7818ce
        j = i + 1
        x = li[i]
        while j < len(li) and li[j] > x:
            li[j - 1] = li[j]
            j = j + 1
        li[j - 1] = x
    return li

<<<<<<< HEAD

def print_list(li: object) -> object:
=======
def print_list(*li):
>>>>>>> cb2aa518baad3e508ddebe40a0d9c8566c7818ce
    for i in li:
        print(i)


<<<<<<< HEAD
def selection(A: object) -> object:
    b = []
    while len(A) > 0:
        mn = A[0]
        for i in range(0, len(A)):
            if A[i] < mn:
                mn = A[i]
        b.append(mn)
        A.remove(mn)
    return b


def merge(l, b, q, e):
    i = b
    j = q + 1

    tmp = []
    while (i < q + 1) and (j < e + 1):
        if l[i] < l[j]:
            tmp.append(l[i])
            i = i + 1
        else:
            tmp.append(l[j])
            j = j + 1

    if i <= q:
        while i <= q:
            tmp.append(l[i])
            i = i + 1
    elif j <= e:
        while j <= e:
            tmp.append(l[j])
            j = j + 1

    for k in range(0, len(tmp)):
        l[b + k] = tmp[k]

    return l


def mergesort(l, b, e):
    if b < e:
        q = int(math.floor((b + e) / 2))
        mergesort(l, b, q)
        mergesort(l, q + 1, e)
        merge(l, b, q, e)
    return l


def parent(i):
    return i / 1


def right(i):
    return 2 * i + 2


def left(i):
    return 2 * i + 1


def heapify(a, n, i):
    largest = i
    l = left(i)
    r = right(i)
    if l < n and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r < n and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)


def build_heap(a):
    for i in range(len(a), -1, -1):
        heapify(a, len(a), i)


def heapsort(l):
    build_heap(l)
    n = len(l)
    for i in range(n - 1, 0, -1):
        l[i], l[0] = l[0], l[i]
        heapify(l, n, 0)
    return l


def partition(a, b, e):
    x = a[e]
    i = b - 1
    for j in range(b, e + 1):
        if a[j] < x:
            i = i + 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[e] = a[e], a[i + 1]
    return i + 1


def quicksort(a, b, e):
    if b < e:
        q = partition(a, b, e)
        quicksort(a, b, q - 1)
        quicksort(a, q + 1, e)


def randomized_partition(a, b, e):
    i = randrange(b, e)
    a[b], a[i] = a[i], a[b]
    return partition(a, b, e)


def randomized_quicksort(a, b, e):
    if b < e:
        q = randomized_partition(a, b, e)
        randomized_quicksort(a, b, q - 1)
        randomized_quicksort(a, q + 1, e)


def stooge_sort(a, i, j):
    if a[i] > a[j]:
        a[i], a[j] = a[j], a[i]
    if i + 1 >= j:
        return
    k = math.floor((j - i + 1) / 3)
    stooge_sort(a, i, j - k)
    stooge_sort(a, i + k, j)
    stooge_sort(a, i, j - k)


def counting_sort(a, k):
    count = []
    for i in range(0, k):
        count.append(0)
    for x in range(0, len(a)):
        count[a[x]] += 1
    x=0
    for i in range(0,len(a)):
        for j in range(0,count[i]):
            a[x]=i


def radix_sort(a, d):  # sortowanie pozycyjne nastawione na minimalizacje złożoności pamięciowej ztąd użycie quicksorta
    for i in a:
        str(i);
    



def bucket_sort(a):
    min = 0
    max = 100

    iw = [0] * (max)
    for i in range(min, max):
        iw[i] = 0
    for j in range(0, len(a)):
        iw[a[j]] += 1
    k = 0
    for l in range(min, max):
        while iw[l] > 0:
            a[k] = l
            iw[l] -= 1
            k += 1


l = [77, 26, 84, 26, 84, 25, 25, 70, 23, 70, 23, 40, 86, 35]
# l = insertion(l)
# print_list(l)
# l = insertion_reverse(l)
# l = selection(l)
# l = mergesort(l, 0, len(l) - 1)
# l = heapsort(l)  nie dziala poprawnie!!!
# quicksort(l, 0, len(l) - 1)
# randomized_quicksort(l, 0, len(l) - 1)
# stooge_sort(l, 0, len(l) - 1)
counting_sort(l,87)
# radix_sort(l, 2) do sprawdzenia !!! to chyba nie ma tak wyglądać
bucket_sort(l)
=======
l = [77, 26, 84, 26, 84, 25, 25, 7, 23, 7, 23, 4, 86, 35]
#l = insertion(l)
#print_list(l)
l=insertion_reverse(l)
>>>>>>> cb2aa518baad3e508ddebe40a0d9c8566c7818ce
print_list(l)
