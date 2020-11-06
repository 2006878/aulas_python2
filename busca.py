#busca linear, podemos usar o in ou o index.
l=[7,6,3,4]
#com o in
print(3 in l)
print(8 in l)
x=eval(input('Busque um elemento na lista: '))
print(x in l)
#com o index
print(l.index(3))
print(l.index(5))
x=eval(input('Busque um elemento na lista: '))
print(l.index(x))
#busca binária
l.sort()
print(l)

def busca_binaria(l, x, início, fim):
    meio = (início+fim)//2
    
    if fim < início:
        return -1

    if x == l(meio):
        return meio

    if x < l(meio):
        return busca_binaria(l, x, início, meio-1)

    if x > l(meio):
        return busca_binaria(l, x, meio +1, fim)

import random

l = random.sample(range(100), 20)
print('Lista original: ', l)
l.sort()
print('Lista ordenada: ',l)
x = eval(input('Digite um número para busca: '))
print(busca_binaria(l, x, 0, 19))

