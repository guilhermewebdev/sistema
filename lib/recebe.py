#!../bin/python3
#codig: utf-8
import datetime
from pprint import pprint

from lib.crud import Crud


# classe que determina a entrada de dados

class Captura:

    # Construtor
    def __init__(self):
        self.__crud = Crud()
        self.__titulo = {'valor': 0, 'nf': bool(), 'recebedor': '', 'data': datetime.datetime.now()}
        self.__valor = 0
        self.__saida = 0
        self.__nf = bool()
        self.__recebedor = ''
        self.__pagador = ''
        self.__referencia = ''

    # Função que captura as informações fornecidas pelo usuário
    def titulo(self, tipo):

        # Loop que finaliza ao receber um valor válido referente ao valor a ser tratado
        while(True):
            if(tipo == 'entrada'):
                self.__valor = input('Digite o valor recebido: \nR$')
            elif(tipo == 'saida'):
                self.__valor = input('Digite o valor a ser pago: \nR$')

            # Formata o valor recebido para dinheiro
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

        # Loop que finaliza ao receber uma informação válida sobre a existência de notas fiscais
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

        # Recebe a referência do pagamento
        self.__referencia = input('Qual a referência do pagamento?\n')

        # Loop que finaliza ao receber um valor válido sobre no nome do recebedor
        while (True):
            self.__recebedor = input('Nome do recebedor: \n')
            if (self.__recebedor.isalpha()):
                self.__titulo['recebedor'] = self.__recebedor
                break
            elif (self.__recebedor == ''):
                return 0
            else:
                print('Digite apenas letras!')

        # Loop que finaliza ao receber um valor válido sobre no nome do pagador
        while (True):
            self.__pagador = input('Nome da pessoa que pagou: \n')
            if (self.__pagador.isalpha()):
                self.__titulo['recebedor'] = self.__pagador
                break
            elif (self.__pagador == ''):
                return 0
            else:
                print('Digite apenas letras!')

        # Grava no banco de dados as informações
        if(self.__titulo['valor'] != 0):
            if(tipo == 'entrada'):
                return self.__crud.gravar_recebimento(self.__titulo)
            elif(tipo == 'saida'):
                return self.__crud.gravar_pagamento(self.__titulo)
            else:
                return 0
        else:
            return 0
