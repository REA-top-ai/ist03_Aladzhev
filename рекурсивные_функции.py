def srecurs(n):
    if n == 1:
        return 1
    return n * srecurs(n - 1)



def bezrec(n):
    c = 1
    for i in range(1, n + 1):
        c *= i
    return c

#Метод без рекурсии быстрее
a= [1, 2, 3, 4, 5]
def srecurs1(spis):
    if not(spis):
        return []
    else:
        return [spis[0] ** 2] + srecurs1(spis[1:])

def bezrec1(spis):
    otv = []
    for i in range(len(spis)):
        otv.append(spis[i] ** 2)
    return otv


