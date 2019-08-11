def insertion(li: object) -> object:
    for i in range(1, len(li)):
        j = i - 1
        x = li[i]
        while j >= 0 and li[j] > x:
            li[j + 1] = li[j]
            j = j - 1
        li[j + 1] = x
    return li

def insertion_reverse(li: object) -> object:
    for i in range(len(li)-1, 0, -1):
        j = i + 1
        x = li[i]
        while j < len(li) and li[j] > x:
            li[j - 1] = li[j]
            j = j + 1
        li[j - 1] = x
    return li

def print_list(*li):
    for i in li:
        print(i)


l = [77, 26, 84, 26, 84, 25, 25, 7, 23, 7, 23, 4, 86, 35]
#l = insertion(l)
#print_list(l)
l=insertion_reverse(l)
print_list(l)
