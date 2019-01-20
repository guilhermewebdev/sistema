#!bin/python3
#codig: utf-8

from pprint import pprint
from lib.recebe import Captura

pprint("         Bem vindo ao Contabil!           ")

captura = Captura()

captura.titulo('entrada')
captura.titulo('saida')