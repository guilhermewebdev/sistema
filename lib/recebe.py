#!../bin/python3
#codig: utf-8
from pprint import pprint
# classe que determina a entrada de dados

class Captura:
    def __init__(self):
        self.__titulo = {}
        self.__valor = 0
        self.__saida = 0
        self.__nf = bool()
        self.__referencia = ''

    def titulo(self, tipo):
        while(self.__valor != '' and self.__nf != ''):
            while(True):
                self.__valor = input('\nDigite o valor recebido: ')
                if(self.__valor.isdigit()):
                    self.__titulo = {'entrada': float(self.__valor)}
                    break
                elif(self.__valor == ''):
                    return 0
                else:
                    print('\n ===== Digite apenas números! =====\n')
            while(True):
                self.__nf = input('\nPossui nota fiscal? [s/n]')
                if(self.__nf == 's' or self.__nf == 'S'):
                    self.__titulo = {'nf': True}
                    break
                elif(self.__nf == 'n' or self.__nf == 'N'):
                    self.__titulo = {'nf': False}
                    break
                elif(self.__nf == ''):
                    return 0
                else:
                    pprint(' ==== Digite apenas "s" para Sim e "n" para não! ====')

            self.__referencia = input('\nQual a referência do pagamento?\n')

            print('\n Digite um novo título ou pressione "Enter" para cancelar. \n')
        if(self.__titulo != {}):
            if(tipo == 'entrada'):
                pass
            elif(tipo == 'saida'):
                pass
            else:
                pass
            return self.__titulo
        else:
            return 0
