#!/usr/bin/python3.6
#coding: utf-8
from cores import CorDeFundo,CorDaLetra
import time
import copy


class Grafo():

    def __init__(self, vertices):
        self.V = vertices
        self.arestas = [[0 for coluna in range(vertices)]
                      for linha in range(vertices)]

    def retornaVertices(self):
        return self.V

    def retornaArestas(self):
        return self.arestas

    #DESCOBRIR OS CAMINHOS E AS CIDADES (ARESTAS E VÉRTICES) VALIDOS E TOTAIS
    def cityWays(self,lista_cidades,lista_caminhos,lista_caminhos_completo):
        i = 0
        #MOSTRA VÉRTICES E CAMINHOS NÃO REPETIDOS RETIRADOS DA MATRIZ DE ADJACENCIA, O INTUITO
        #É SABER OS CAMINHOS ÚNICOS, CONHECER TODOS OS VÉRTICES, ARESTAS E VÉRTICES OS  QUAIS
        #CONECTAMOS CAMINHOS

        for vertex in range(len(self.arestas)):
            #INICIA EM i PARA EXCLUIR CAMINHOS JÁ VISTOS
            for path in range(i,len(self.arestas[vertex])):
                #NÃO PODE ADICIONAR ARESTA COM VALOR ZERO OU NEGATIVO, JA QUE SE TRATAM DE DIS-
                #TANCIAS, TEMOS QUE CONSIDERAR QUE NÃO HÁ CAMINHO
                if(self.arestas[vertex][path] >= 0):
                    #SE O INDICE vertex FOR IGUAL AO INDICE path, TEMOS ENTÃO QUE  TRATA-SE DA
                    #DISTANCIA DE UM VERTICE PARA ELE MESM0, POR ISSO CONSIDERAMOS COMO UM CA-
                    #MINHO INEXISTENTE NÃO ADICIONADO À lista_caminhos
                    if (vertex == path):
                        lista_cidades.append(vertex)
                    else:
                        lista_caminhos.append([self.arestas[vertex][path],[vertex,path]])
            i += 1

        #COLOCANDO TODOS OS VALORES DISPONIVEIS PARA USO EM UM MATRIZ
        for vertex in range(len(self.arestas)):
            lista = []
            for path in range(len(self.arestas[vertex])):
                    lista.append([self.arestas[vertex][path],[vertex,path]])
            lista_caminhos_completo.append(lista)

    #ADICIONA À LISTA DE VISITADOS OS ELEMENTOS QUE FOREM PASSADOS PARA O MÉTODO, CASO SEJAM
    #REPETIDOS, O PRÓPRIO MÉTODO TRATARÁ ISSO
    def addVisitado(self,visitado,cidade,vertice):#, caminhos_completos, caminhos_usados):
        #SE FOR UMA LISTA VAZIA, ENTÃO É O PRIMEIRO ELEMENTO
        if (visitado):
            #for i in range(len(visitado)):
                #print("VISITADO",visitado[i], cidade[vertice])
                #if (visitado[i] != cidade[vertice]):
                print("CIDADE VERTICE",cidade[vertice])
                visitado.append(cidade[vertice])
        else:
            visitado.append(vertice)
        print ("V",vertice)


    #DEFINE A ARESTA E O CAMINHO QUE TEM CONEXÃO
    def quemVejo(self,i,caminhos):
        vertices_visualizados = []
        #VERIFICA-SE  A LINHA QUE FOI ENVIADA MEDIANTE i E DESCOBRIMOS TODOS OS VALORES QUE
        #SAEM DO VÉRTICE.
        for j in range (len(caminhos)):
            if(caminhos[i][j][0] != 0):
                vertices_visualizados.append([caminhos[i][j][0],caminhos[i][j][1][1]])
                print('VERTICE VISUALIZADOS',vertices_visualizados)

        return vertices_visualizados

    def calculaRota(self, rota, caminhos_completos, path):
        print("------------")
        distancia_total = 0
        #DEFINE (EM ORDEM DE ROTA) OS CAMINHOS NECESSÁRIOS PARA O GRAFO
        for k in range(len(rota)-1):
            for i in range(len(caminhos_completos)):
                for j in range (len(caminhos_completos[i])):
                    if rota[k] == caminhos_completos[i][j][1][0] and rota[k+1] == caminhos_completos[i][j][1][1]:
                        path.append(caminhos_completos[i][j][0])
                #     print(rota[k]," e ",rota[k+1])
                # print(caminhos_completos[i][j][1][0], " e ", caminhos_completos[i][j][1][1])
        print(path)
        #CALCULA A DISTANCIA TOTAL DO CAMINHO
        for i in range(len(path)):
            distancia_total += path[i]

        return distancia_total

    def heapMove(self, tam, lista, comb, inicio_e_fim):
        print("LISTA PASSADA",lista)

        c = 0
        if tam == len(lista):    #ADICIONA A LISTA ORIGINAL
            lista_aux = copy.deepcopy(lista)
            lista_aux.append(inicio_e_fim)
            lista_aux.insert(0,inicio_e_fim)
            comb.append(lista_aux)

        while True:
            if tam > 2:
                print("LISTA 1", lista[:tam])
                self.heapMove(tam-1, lista, comb, inicio_e_fim)
            if tam <= c + 1:
                print("C",c," e N ", tam)
                break
            elif tam % 2 == 1: #SE O TAMANHO É IMPAR, TROCAMOS O PRIMEIRO E O ULTIMO ELEMENTO
                print("LISTA 2", lista[:tam])
                lista[0], lista[tam-1] = lista[tam-1], lista[0]
            else:
                print("LISTA 3", lista[:tam]) #SE O TAMANHO É PAR, TROCA-SE O i-ESIMO ELEMENTO E O UTIMO
                lista[c], lista[tam-1] = lista[tam-1], lista[c]

            lista_aux2 = copy.deepcopy(lista)
            lista_aux2.append(inicio_e_fim)
            lista_aux2.insert(0,inicio_e_fim)
            comb.append(copy.deepcopy(lista_aux2))

            c += 1
            print("C",c," e N ", tam)