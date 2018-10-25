#!/usr/bin/python3.6
#coding: utf-8

class leArquivo():
    def __init__ (self,nome):
        #ATRIBUTO É O CAMINHO DO ARQUIVO LIDO
        self.nome = nome

    def le(self):
        #LE A PRIMEIRA LINHA E ARMAZENA NUMA VARIÁVEL VÉRTICE
        arquivo = open(self.nome, 'r')
        grafo = []
        i = 0
        for line in arquivo:
            #SEPARA AS LINHAS, CADA UMA DAS LINHAS DO ARQUIVO SE TORNAM UMA LISTA PORTANTO TEMOS
            #UM GRAFO ONDE O PRIMEIRO ELEMENTO É A QUANTIDADE DE GRAFOS E O RESTANTE AS ARESTAS
            grafo.append(list(map(int,line.split())))
            i = i + 1
        arquivo.close()

        return grafo