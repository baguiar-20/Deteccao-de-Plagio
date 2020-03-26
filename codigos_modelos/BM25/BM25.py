import numpy as np
import math as mt
import glob
import re

# ainda falta testar 


def mediaDoc(tamLista, qtdLista):
    avg_doclen = 0
    md = 0
    for x in tamLista:
        md += tamLista[x]
    if qtdLista !=0:
        avg_doclen = md/qtdLista
    else:
        avg_doclen = md
    return avg_doclen


def termosConsulta(doc): #numero de termos do documento que ocorre na consulta
    query = []
    termosConsulta = {}
    cont = 0
    d = {}
    for i in doc:
        for j in i.items():
            query = j
            for t in doc:
                for k in t.items():
                    consulta = k
                    for c in query[1]:
                        d = consulta[1].count(c)
                        termosConsulta[cont] = [query[0],consulta[0], c, d]
                        cont += 1
    return termosConsulta


def OkapiBM25(docs,cont_termos, avg_doclen, qtdDocs,termosConsulta, tam_colecao, K1 = 1, b = 0.75):
    idf = 0
    tabela = {}
    cont = 0
    bm = 0.0
    okapi = {}
    for i in docs:
        for j in i.items():
            busca = j
            #print("busca",busca)
            for t in docs:
                for k in t.items():
                    consulta = k
                    for i,j in cont_termos.items():
                        if (i in busca[1]) and (i in consulta[1]):
                            idf =  mt.log1p((qtdDocs-j + 0.5)/(j+0.5))
                            for x in termosConsulta:
                                if (termosConsulta[x][2] == i):
                                    a = termosConsulta[x][3]
                            for x in tam_colecao:
                                for t in x.items():
                                    if(consulta[0] == t[0]):
                                        tam = t[1]
                            #print(idf, a, tam, avg_doclen)
                            bm += idf * ((a *(K1+1))/(a + K1*((1-b)+b*(tam/avg_doclen))))
                    #print('troca', bm)
                    okapi[cont] = [busca[0], consulta[0], bm]
                    cont += 1
                    bm = 0
                    #print(busca[0], consulta[0], bm)        
    return okapi
