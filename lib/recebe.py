#!../bin/python3
#codig: utf-8
import datetime
from pprint import pprint

from lib.crud import Crud


# classe que determina a entrada de dados

class Captura:
    def __init__(self):
        self.__crud = Crud()
        self.__titulo = {'valor': 0, 'nf': bool(), 'recebedor': '', 'data': datetime.datetime.now()}
        self.__valor = 0
        self.__saida = 0
        self.__nf = bool()
        self.__pessoa = ''
        self.__referencia = ''

    def titulo(self, tipo):
        while(self.__valor != '' and self.__nf != ''):
            while(True):
                self.__valor = input('Digite o valor recebido: \n')
                nar = self.__valor.split('.')
                if((len(nar) == 1 or len(nar) == 2) and nar[0].isdigit()):
                    if(len(nar) == 2):
                        if(nar[1].isdigit()):
                            self.__titulo['valor'] = round(float(self.__valor), 2)
                            break
                        else:
                            print('\n ===== Digite apenas números! =====\n')
                    else:
                        self.__titulo['valor'] = round(float(self.__valor), 2)
                        break
                elif(self.__valor == ''):
                    return 0
                else:
                    print('\n ===== Digite apenas números! =====\n')
            while(True):
                self.__nf = input('Possui nota fiscal? [s/n]\n')
                if(self.__nf == 's' or self.__nf == 'S'):
                    self.__titulo['nf'] = True
                    break
                elif(self.__nf == 'n' or self.__nf == 'N'):
                    self.__titulo['nf'] = False
                    break
                elif(self.__nf == ''):
                    return 0
                else:
                    pprint(' ==== Digite apenas "s" para Sim e "n" para não! ====')

            self.__referencia = input('Qual a referência do pagamento?\n')

            while (True):
                self.__pessoa = input('Nome do recebedor: \n')
                if (self.__pessoa.isalpha()):
                    self.__titulo['recebedor'] = self.__pessoa
                    break
                elif (self.__pessoa == ''):
                    return 0
                else:
                    print('Digite apenas letras!')
            print('\nDigite um novo título ou pressione "Enter" para finalizar. \n')

        if(self.__titulo['valor'] != 0):
            if(tipo == 'entrada'):
                pass
            elif(tipo == 'saida'):
                pass
            else:
                pass
            self.__crud.gravar_recebimento(self.__titulo)
            return self.__titulo
        else:
            return 0
