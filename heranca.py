import random

class MyList(list): #(list) é a classe pai ou base
    def choice(self):
        return random.choice(self)
l = MyList ([1,3,2,6])
print('MyList = ', l)
print('Tamanho de MyList = ', len(l))
print('Número aleatório de MyList = ', l.choice())