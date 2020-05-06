import numpy as np
import math as mt
import glob

'''fórmula  para IDF tem desvantagens para termos que aparecem em mais da 
metade dos documentos do corpus. 
Se o numero de doc que contem o termo (ni) > N/2, 
o termo negativo sera incluido no calculo '''

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

def normaliza(docs_colecao):
    lista_colecao = []
    for i in docs_colecao:
        c = i
        for t in c.items():
            lista_colecao.append(t)
    return lista_colecao


def termosDeConsulta(docs_colecao): #numero de termos que ocorre na consulta
    termosConsulta = {}
    cont = 0
    for i in docs_colecao:
        for j in docs_colecao:
            for x in j[1]:
                d = i[1].count(x)
                termosConsulta[cont] = [i[0],j[0], x, d]
                cont += 1
    return termosConsulta



def OkapiBM251(docs_colecao,cont_termos, avg_doclen, qtdDocs,termosConsulta, tam_colecao, K1 = 1, b = 0.75):
    idf = 0
    a = 0
    okapi = {}
    cont = 0
    bm = 0.0
    for busca in docs_colecao:
        for consulta in docs_colecao:
            for term, num in cont_termos.items():
                if (term in busca[1]) and (term in consulta[1]):
                    idf = mt.log(1+((qtdDocs-num + 0.5) / (num +0.5)))
                    for x in termosConsulta:
                        if (termosConsulta[x][0] == busca[0] and termosConsulta[x][0] == consulta[0] and termosConsulta[x][2] == term):
                            a = termosConsulta[x][3]
                    for t in range(len(tam_colecao)):
                        if(consulta[0] == tam_colecao[t][0]):
                            tam = tam_colecao[t][1]
                    bm += idf * ((a *(K1+1)) / (K1 * ( (1-b) + b *(tam/avg_doclen) ) + a))
                    print(term, a, K1+1, a *(K1+1))
            okapi[cont] = [busca[0], consulta[0], bm]
            cont += 1
            bm = 0        
    return okapi


'''/

def OkapiBM25(docs_colecao,cont_termos, avg_doclen, qtdDocs,termosConsulta, tam_colecao, K1 = 1, b = 0.75):
    idf = 0
    cont = 0
    bm = 0.0
    okapi = {}
    for i in docs_colecao: #dicionario {chave: doc, [hgdshdjfhjdfhjdfhjh], chave: doc, [hdhfhdgfhdg]}
        busca = i[1] #[hgdshdjfhjdfhjdfhjh]
            for j in docs_colecao:
                consulta = j[1] #[hdhfhdgfhdg]
                    for i,j in cont_termos.items(): # quia: 10
                        if (i in busca[1]) and (i in consulta[1]): # se o termo quia aparecer no documento de busca e de consulta bla bla
                            idf =  mt.log((qtdDocs-j + 0.5)/(j+0.5)) # calcula essa merda aqui
                            for x in termosConsulta: # x é um contador nos termos da consulta
                                if (termosConsulta[x][2] == i): #retorna o documento de busca, documento de consulta, o termo semelhante e a quantidade de vezes que ele se repete, se o termo semelhante é igual ao termo quia
                                    a = termosConsulta[x][3] # a recebe quantidade de vezes que o termo se repete
                            for x in tam_colecao: # x é um cpntador no tam_colecao
                                for t in x.items(): 
                                    if(consulta[0] == t[0]): # se a consulta for igual ao doc que tem o seu tamanho 
                                        tam = t[1]#tamanho do doc que eu to consultando
                            bm += idf * ((a *(K1+1))/(K1 * ((1-b)+b*(tam/avg_doclen)) + a)) #continha
                    okapi[cont] = [busca[0], consulta[0], bm] #continha 
                    cont += 1
                    bm = 0       
    return okapi








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

'''
