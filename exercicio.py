# Elabore um programa para manipular informações em uma lista.
# Os itens da lista deverão ser arquivos de informática
# A cada operação executada (leitura, inserção, exclusão e edição da lista deverá gravar um log)
# O arquivo será "log.txt"
# Implementar a função grava log e demais funções em arquivo separado.
# A função gravaLog deverá receber uma mensagem de parâmetro que será gravada.
# Tempo estimado: 20 minutos
import execucao
import os
import time

op = 0
lista = []
while (op != 5 ):
    time.sleep(3)
    os.system('cls')
    op = int(input('Operação desejada \n' +
                    '1- CADASTRAR  | 2- VISUALIZAR \n' +
                    '3- ALTERAR    | 4- EXCLUIR \n ' +
                    '            5-SAIR\n'))
    match op:
        case 1 :
            execucao .gravaLog('Opção Cadastrar\n')
            valor = input('INFORME O ITEM QUE DESEJA CADASTRAR: ')
            print(execucao.inserir(lista,valor))

        case 2 :
            execucao .gravaLog('Opção Listar\n')
            execucao.exibir(lista)
        case 3 :
            execucao .gravaLog('Opção Alterar\n')
            valor = input('QUAL O ITEM QUE DESEJA ALTERAR: ')
            execucao.alterar(lista,valor)
        case 4 :
            execucao .gravaLog('Opção Excluir\n')
            valor = input('ITEM QUE DESEJA EXCLUIR: ')
            execucao.excluir(lista,valor)
        case 5 :
            execucao .gravaLog('Obrigado por usar o nosso Sistema\n')
            print('SAINDO')
            break
        case outrocaso:
            execucao .gravaLog('Opção Invalida')
            print('OPÇÃO INVALIDA')
