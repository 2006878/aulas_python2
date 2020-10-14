def readFile(filename): #leitura do arquivo
    infile = open(filename, 'r') #abrir no modo leitura
    content = infile.read() #leitura do arquivo inteiro e armazena o em content
    infile.close() #fecha o arquivo
    wordList = content.split() #divide em tokens ou palavras
    print(wordList) #imprime lista de palavras
    return len(wordList), len(content) #retorna quantidade de palavras e quantidade de caracteres

arq = input('Digite o nome do arquivo: ')
n_words, n_chars = readFile(arq) #chama a função readfile e o usa no arquivo teste.txt
print(n_chars) #imprime número de caracteres
print(n_words) #imprime número de palavras
