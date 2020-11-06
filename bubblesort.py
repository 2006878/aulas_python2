''' Esse método de busca percorre o conjunto várias vezes,
e a cada iteração compara o ítem atual ao seu sucessor e troca os de lugar caso estejam na ordem incorreta'''
#para um vetor de n elementos, são necessárias n-1 iterações
def bubble_sort(v):
    for i in range(len(v)-1):
        for j in range(len(v)-i-1):
            if(v[j]>v[j+1]):
                v[j], v[j+1] = v[j+1], v[j]

def insertion_sort(v):
    for i in range(1, len(v)):
        x=v[i]
        j=i-1
        while j>=0 and x<v[j]:
            v[j+1]=v[j]
            j-=1
        v[j+1]=x

v=[1,3,2,4,7,6,9,5,9,0]#vetor original com números
animal=['cão', 'urubú', 'gato', 'cavalo', 'aranha']#vetor original com strings
print('Original: ',v)
bubble_sort(v)
print('Bubble Sort: ',v)
insertion_sort(v)
print('Insertion Sort: ',v)        

print('Original: ',animal)
bubble_sort(animal)
print('Bubble Sort: ',animal)
print('Insertion Sort: ', animal)