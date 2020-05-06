import glob
import re
import funcaoPreC as fpre
import BM25 as bm25
import timeit
from pathlib import Path
import os

import math

# processar os tokens antes para o pre processamento


docs_colecao = []
termos_colecao_c = []
tam_colecao = []
list_c = []
score = []
tam_list_c = []

tam_doc= {}
tam_list = {}

cont = 0
qtdDocs = 0

 

tokensSymC = fpre.token("tokenSymbolsC.txt")

p = os.getcwd() + '/testeFakes/testeP'

with os.scandir(p) as arqs:
    for arq in arqs:
        if arq.name.endswith('.c') and arq.is_file():
            with open(arq.path, 'r') as codigo:
                codeTEXT = codigo.readlines()
                texto = fpre.removeSpace(codeTEXT)
                texto = fpre.tokensS(codeTEXT, tokensSymC)
                texto = fpre.tokensP(codeTEXT)
                texto = fpre.normaliza(codeTEXT)
                qtdDocs += 1
                texto = fpre.calcNgram(texto, 4)
                tam_doc = len(texto)
                tam_list[qtdDocs] = len(texto)
                termos = texto
                termos_colecao_c += termos
                docs_colecao, tam_colecao = fpre.insertTERMOS(arq.name, termos, list_c, tam_list_c, tam_doc)
docs_colecao = bm25.normaliza(docs_colecao)
tam_colecao = bm25.normaliza(tam_colecao)
avg_doclen = bm25.mediaDoc(tam_list, qtdDocs)
cont_termos = fpre.preencheTERMOS(termos_colecao_c, list_c)
termosConsulta = bm25.termosDeConsulta(docs_colecao) 


score = bm25.OkapiBM251(docs_colecao, cont_termos, avg_doclen, qtdDocs, termosConsulta, tam_colecao)
print(score)
 

'''
#score = bm25.OkapiBM251(docs_colecao, cont_termos, avg_doclen, i, termosConsulta, tam_colecao)
#print(score)
#retorna o documento de busca, documento de consulta, o termo semelhante e a quantidade de vezes que ele se repete

#print()
#print(termosConsulta)
#print("Numero total de documentos: ", i)
#print()
#print("Tamanho de cada documento: ")
#print(tam_colecao)
#print()
#print("Media dos documentos(avg_doclen): ", avg_doclen)
#print()
#print("Nº de documentos em q o termo ocorre na coleção", cont_termos)
#print()

#print("Numero de termo da consulta ocorre no documento: ") 
#print(termosConsulta)

#score = bm25.OkapiBM25(docs_colecao, cont_termos, avg_doclen, i, termosConsulta, tam_colecao)

#print(score)


#print(len(docs_colecao))

