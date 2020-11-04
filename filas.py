#fila, é uma estrutura para armazenar elementos, quem entra entra no fim da fila e quem sai é o primeiro elemento  
class fila():
    def __init__(self):
        self.data = []

    def inserir(self, x):
        self.data.append(x)

    def remover(self, x):
        if len(self.data) > 0:
            return self.data.pop(0)

    def top(self, x):
        if len(self.data) > 0:
            return self.data(0)

    def empty(self):
        return not len(self.data) > 0

f = fila()





