# EXCEÇÃO

#não usr muito try/except

#Usar somente em ultimos casos.

try:
    try:
        try:
            vl1 = int(input('Informe um valor inteiro: '))
            vl2 = int(input('Informe outro valor inteiro: '))
            print('O resultado da divisão dos valores é ' + str(vl1/vl2))
            print('Obrigado por usar nosso sistema')
        except NameError:
            print('Alguma Variavel não existe')
        except ZeroDivisionError:
            print('Impossiveis dividir por zero')
        except ValueError:
            print('Algum valor invalido foi passado')
        except TypeError:
            print('Tipo de dado invalido')
        except:
            print('Algo deu errado')
    except:
        print('Erro ao imformar o primeiro valor.')
except:
    print('Erro ao efetuar a divisão')
    