#!/usr/bin/python3.6
#coding: utf-8
from caixeiro_viajante import Grafo
from arquivo import leArquivo
from cores import CorDaLetra,CorDeFundo
import sys
import copy

#DEFINE
VERTICE_INICIO = int(sys.argv[2])

#LISTAS INSTANCIADAS
arestas = []
lista_cidades = []
lista_caminhos = []
lista_caminhos_completo = []
visitado = []
disponiveis =[]
percebido_ordenado = []
ordenado = []
path = []
caminhos_usados = []
combinatoria = []
rotas_combinadas = []

#INSTANCIA OBJETO DA CLASSE COR PARA PODER USAR MAIS FACILMENTE A PROPOSTA DO
l_cor = CorDaLetra()
f_cor = CorDeFundo()
#CRIAÇÃO DO OBJETO INSTANCIA PASSANDO UM ARGUMENTO RECEBIDO DA LINHA DE COMANDO
#CONTENDO O CAMINHO\NOME DO ARQUIVO A SER INTEPRETADO
instancia = leArquivo(sys.argv[1])
dados = instancia.le()

#TORNANDO DADOS ILEGIVEIS VINDO DE UM METODO E ATRIBUINDO-OS PARA VARIÁVEIS MAIS
#FÁCEIS DE SE COMPREENDER SUAS FUNÇÕES
vertices = dados[0][0]
arestas = dados[1:]

#INSTANCIAÇÃO DE GRAFOS E ATRIBUIÇÃO DOS VÉRTICES
g = Grafo(vertices)
g.arestas = arestas

print(l_cor.vermelho," #---> VERTICE",g.retornaVertices(),l_cor.original)
print(l_cor.ciano," #---> ARESTAS",g.retornaArestas(),l_cor.original)



'''
MÉTODO g.cityWays(x,y,z)
**** Descrição:
DEVOLVE OS CAMINHOS E AS CIDADES DE UM GRAFO RETIRADAS DA MATRIZ DE ADJACENCIA

**** Dados:
| x |---lista_cidades ---> lista      EX:. [0, 1, 2]
| = | +-DESCR: Vértices ou cidades
| y |---lista_caminhos ---> lista      EX:. [[22, [0, 1]], [20, [0, 2]],...]
| = | +-DESCR: Corresponde aos caminhos válidos
| z |---lista_caminhos_completos ---> lista      EX:. [[[0, [0, 0]], [22, [0, 1]], [20, [0, 2]]],...]
| = | +-DESCR: Todos os caminhos disponíveis inclusive os zeros
'''
g.cityWays(lista_cidades,lista_caminhos,lista_caminhos_completo)
print(f_cor.azul,"---> CIDADES   : ",l_cor.original,lista_cidades)
print(f_cor.azul,"---> CAMINHOS  : ",l_cor.original,lista_caminhos)
print(f_cor.azul,"---> CAMINHOS COMPLETOS  : ",l_cor.original,lista_caminhos_completo)

#CRIA CÓPIA DA LISTA DE CIDADES PARA SABER QUAIS ESTÃO DISPONÍVEIS PARA SER ADI-
#CIONADAS FUTURAMENTE
disponiveis = copy.deepcopy(lista_cidades)
print("----->",disponiveis)

'''
MÉTODO g.addVisitado(x,y,z)
**** Descrição:
ADICIONA O PRIMEIRO ELEMENTO À LISTA DE VISITADOS, SENDO ASSIM O PRIMEIRO ELE-
MENTO É A CIDADE DE PARTIDA INICIAL (OBS: SÓ ADICIONA O VÉRTICE SE ELE JÁ NÃO
ESTIVER PRESENTE NA LISTA DE VISITADOS)

**** Dados:
| x |---visitado ---> lista   EX:. [0,2]
| = | +-DESCR: vértice
| y |---lista_cidades ---> lista      EX:. [1,2,3]
| = | +-DESCR: lista de cidades
| z |---VERTICE_INICIO ---> inteiro    EX:. 0
| = | +-DESCR: cidade inicial (vértice de inicio - referencia)
'''
#g.addVisitado(visitado, lista_cidades,VERTICE_INICIO, lista_caminhos_completo, caminhos_usados)
g.addVisitado(visitado, lista_cidades,VERTICE_INICIO)

print(l_cor.amarelo,"PRIMEIRO VÉRTICE ADICIONADO", visitado,l_cor.original)


while(len(visitado) < len(lista_cidades)):
    '''
    MÉTODO g.quemVejo(x,y)
    **** Descrição:
    PEGA O ULTIMO ELEMENTO DA LISTA (lista[-1] -> corresponde ao ultimo elemento da lista)
    E IDENTIFICA QUAIS VÉRTICES CONSEGUE VER E SEUS CAMINHOS DIFERENTES DE ZERO
    **** Dados:
    | x |---visitado[-1] ---> elemento do final da lista    EX:. [1,2,3] -> 3
    | = | +-DESCR: vértice
    | y |---lista_caminhos_completos ---> lista      EX:. [[[0, [0, 0]], [22, [0, 1]], [20, [0, 2]]],...]
    | = | +-DESCR: Todos os caminhos disponíveis inclusive os zeros
    *** Retorno:
    VAR: percebido ---> ex:. [[22, 1], [20, 2]]
    DESCR: Retorna os caminhos percebidos do vértice enviado
    '''
    percebido = g.quemVejo(visitado[-1],lista_caminhos_completo)
    print(l_cor.vermelho + f"VISTO PELO ELEMENTO {visitado[-1]}" + l_cor.original)
    for i in range(len(percebido)):
        print(l_cor.magenta,"VÉRTICES ### ",percebido[i][1]," ### ",l_cor.original)
        print(l_cor.ciano,"CAMINHOS --- ",percebido[i][0]," --- ",l_cor.original)

    #ORDENA PELO TAMANHO DA ARESTA PARA SER ESCOLHIDO
    percebido_ordenado = copy.deepcopy(sorted(percebido))
    print(l_cor.verde,"SAÍDA ORDENADA ---> ",percebido_ordenado,l_cor.original)

    '''
    MÉTODO g.addVisitado(x,y,z)
    **** Descrição:
    ADICIONA O PRIMEIRO ELEMENTO À LISTA DE VISITADOS, SENDO ASSIM O PRIMEIRO ELE-
    MENTO É A CIDADE DE PARTIDA INICIAL (OBS: SÓ ADICIONA O VÉRTICE SE ELE JÁ NÃO
    ESTIVER PRESENTE NA LISTA DE VISITADOS)

    **** Dados:
    | x |---visitado ---> lista   EX:. [0,2]
    | = | +-DESCR: vértice
    | y |---lista_cidades ---> lista      EX:. [1,2,3]
    | = | +-DESCR: lista de cidades
    | z |---VERTICE_INICIO ---> inteiro    EX:. 0
    | = | +-DESCR: cidade inicial (vértice de inicio - referencia)
    '''
    print("Perceb ordenado",percebido_ordenado)
    flag = True
    k = 0
    #SE A CIDADE SELECIONADA ESTIVER EM VISITADOS, NÃO É ADICIONADA E PASSA PARA A PRÓXI
    #MA CIDADE DE MENOR CAMINHO
    while flag:
        if not lista_cidades[percebido_ordenado[k][1]] in visitado:
            flag = False
            g.addVisitado(visitado, lista_cidades, percebido_ordenado[k][1])
            #g.addVisitado(visitado, lista_cidades, percebido_ordenado[k][1], lista_caminhos_completo, caminhos_usados)
        else:
            k += 1

visitado.append(VERTICE_INICIO)
print(l_cor.amarelo,"VÉRTICE ADICIONADO", visitado,l_cor.original)

'''
MÉTODO g.calculaRota(x,y,z)
**** Descrição:
ADICIONA O PRIMEIRO ELEMENTO À LISTA DE VISITADOS, SENDO ASSIM O PRIMEIRO ELE-
MENTO É A CIDADE DE PARTIDA INICIAL (OBS: SÓ ADICIONA O VÉRTICE SE ELE JÁ NÃO
ESTIVER PRESENTE NA LISTA DE VISITADOS)

**** Dados:
| x |---visitado ---> lista   EX:. [0,2]
| = | +-DESCR: vértice
| y |---lista_caminhos_completo  ---> lista      EX:. [[[0, [0, 0]], [22, [0, 1]], [20, [0, 2]]],...]
| = | +-DESCR: Todos os caminhos disponíveis inclusive os zeros
| z |---path ---> lista    EX:. []
| = | +-DESCR: VAZIA A SER RETORNADA
*** Retorno:
VAR: distancia_total ---> ex:. 140
DESCR: Retorna a soma dos caminhos visitados
'''

distancia_total = g.calculaRota(visitado, lista_caminhos_completo, path)
print(l_cor.preto,f_cor.branco,"DISTANCIA",distancia_total,l_cor.original)

'''
MÉTODO g.heapMove(x,y,z)
**** Descrição:
MOVIMENTAÇÃOS DE VÉRTICE OU ALTERAÇÃO DE VIZINHANÇA DE MODO A BUSCAR
CAMINHOS MAIS CURTOS

**** Dados:
| x |---len(visitado[1:len(visitado)-1])---> lista   EX:. [2,3]
| = | +-DESCR: Passa para a função somente valores do meio dos visitados
| y |---lista_cidades ---> lista      EX:. [1,2,3]
| = | +-DESCR: lista de cidades
| z |---VERTICE_INICIO ---> inteiro    EX:. 0
| = | +-DESCR: cidade inicial (vértice de inicio - referencia)
'''
g.heapMove(len(visitado[1:len(visitado)-1]) , visitado[1:len(visitado)-1], combinatoria, VERTICE_INICIO)
print(combinatoria)
print(len(combinatoria))

for i in range(len(combinatoria)):
    path = []
    distancia_total = g.calculaRota(combinatoria[i], lista_caminhos_completo, path)
    print("COMBINATORIA", combinatoria[i])
    print(l_cor.preto,f_cor.branco,"DISTANCIA",distancia_total,l_cor.original)

