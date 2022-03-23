'''from genericpath import exists


if exists('arquivo.txt'):
    arq = open('arquivo.txt','r')
    arq.close
else:
    arq = open('arquivo.txt', 'w')
    arq.close()'''

try:
    arq=open('arquivo.txt','r')
    arq.close()
    print('Arquivo foi aberto para leitura')
except FileNotFoundError:
    print('O arquivo não existe e será criado')
    arq = open('arquivo.txt','w')
    arq.close()
except:
    print('Ocorreu um erro ao tentar abrir o arquivo')

try:
    arq = open('arquivo.txt','w')# sobescreve o que tem escrito.
    arq.write('Ola Mundo \n')
    arq.close()
except:
    print('OCorre algum erro ao tentar escrever no arquivo')
try:
    arq = open('arquivo.txt','a') #adiciona o texto no arquivo
    arq.write('Seja bem vindo a manipulação de texto')
    arq.close()
except:print('Erro ao tentar escrever no arquivo')

try:
    arq = open('arquivo')
    conteudo = arq.read()
    print(conteudo)
    arq.close()
except:
    print('Erro ao abrir o arquivo para leitura.')