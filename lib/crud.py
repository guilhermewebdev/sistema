#../bin/python3
# coding: utf-8

from pprint import pprint

from mongoengine import connect
from pymongo import MongoClient

# Classe para Criar, Ler, Atualizar e Deletar
# Create, read, update e delete
class Crud:

    # Construtor
    def __init__(self):
        self.__cliente = MongoClient('localhost', 27017)
        self.__banco = self.__cliente.banco
        self.__entrada = self.__banco.entrada
        self.__saida = self.__banco.saida
        connect('banco')

    # Grava os recebimentos
    def gravar_recebimento(self, titulo):
        entrada_id = self.__entrada.insert_one(titulo).inserted_id
        print('A idendificação do processamento é: ' + str(entrada_id) + '\n')
        return entrada_id

    # Grava os pagamentos
    def gravar_pagamento(self, titulo):
        saida_id = self.__saida.insert_one(titulo).inserted_id
        print('A idendificação do processamento é: ' + str(saida_id) + '\n')