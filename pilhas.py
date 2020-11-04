#Pilhas, relacionado à estrutura de dados, pilha funciona como uma pilha mesmo e quem sai é sempre o último empilhado
#exemplo de como transformar um número decimal em binário
class Pilha():
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)    


    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(-1)

    def top(self):
        if len(self.data) > 0:
            return self.data[-1]  

    def empty(self):
        return not len(self.data) > 0

p = Pilha()
num = eval(input('Digite um número para ser transformado em binário:  '))
while num > 0:
    resto = num % 2
    num = num//2
    p.push(resto)

while not p.empty():
    print(p.pop())

'''.pop remove o último da pilha
.push adiciona um ítem à pilha
.top verifica o pultimo da fila
.empty verifica se está vazia'''
            
