

# crtl + h = ALTERA PALAVRAS TODAS DE UMA VEZ SÓ


from contextlib import ExitStack
from genericpath import exists


sucesso_Inserir = ' cadastrado com sucesso!'
sucesso_Excluir = ' removido com sucesso!'
lista_Vazia = ' Lista Vazia!'
inexistente = ' não esta cadastrado!'

def inserir (obj,valor):
    obj.append(valor)
    print(valor + sucesso_Inserir)

def excluir (obj,valor):
    if len(obj) == 0:
        print(lista_Vazia)
    if valor in obj:
        obj.remove(valor)
        print( valor + sucesso_Excluir)
    else:
        print(valor + inexistente)

def exibir (obj):
    if len(obj) == 0:
        print('Lista vazia!')
    print(obj)

def alterar (obj, valor):
    if len(obj) == 0:
        print(lista_Vazia)
    if not ( valor in obj):
        print( inexistente)
    novo = input('Informe um novo objeto: ' + valor + ': ')
    for x in range (0,len(obj)):
        if obj[x] == valor:
            obj[x] = novo
            print (valor + ' alterado para ' + novo + '!')

def  gravaLog(mensagem):
    if exists('log.txt'):
        arq = open('log.txt','a')
    else:
        arq = open('log.txt','w')
    arq.write(mensagem)
    arq.close()
