#!bin/python3
#codig: utf-8

from pprint import pprint
from lib.recebe import Captura

pprint("         Bem vindo ao Contabil!           ")

# Função que dá inicio ao programa
def __init__():
    captura = Captura()

    # Loop que recebe a informação sobre o que o usuário quer fazer
    while(True):
        acao = input('Digite o que você quer fazer: \n')

        if(acao == 'receber'):
            captura.titulo('entrada')
        elif(acao == 'pagar'):
            captura.titulo('saida')
        elif(acao == 'ajuda'):
            pprint('')
        elif(acao == 'sair'):
            break
        else:
            print('Comando "' + acao + '" não reconhecido')

    return 0


__init__()