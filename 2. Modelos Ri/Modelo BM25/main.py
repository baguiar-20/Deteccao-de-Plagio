
import funPreGeral as fpg
import funPreC as fpC
import funPrePy as fpPy

import re
import OkapiBM25 as okapibm25
import timeit
from pathlib import Path
import os



docs_colecao = []
termos_colecao = []
tam_colecao = []
lists = []
score = []
tam_list = {}
tam_doc= {}
cont = 0
qtdDocs = 0

 
#processar os tokens antes para o pre processamento
tokensSym = fpg.token("tokenSymbols.txt")


p = os.getcwd() + '/testePy/testesFakesPy'

with os.scandir(p) as arqs:
    for arq in arqs:
        if arq.name and arq.is_file():
            with open(arq.path, 'r') as codigo:
                codeTEXT = codigo.readlines()
                texto = fpg.tokensSimbolos(codeTEXT, tokensSym)

                #substitui palavras reservadas de cada linguagen para tokens
                #remove espaços e comentarios
                if arq.name.endswith('.c'): 
                    texto = fpC.removeEspacoC(codeTEXT)
                    texto = fpC.tokensC(codeTEXT)
                
                elif arq.name.endswith('.py'):
                    texto = fpPy.removeEspacoPy(codeTEXT)
                    texto = fpPy.tokensPy(codeTEXT)
    
                texto = fpg.minusculas(codeTEXT)
                tam_list[qtdDocs] = len(texto)
                qtdDocs += 1
                texto = fpg.calcNgram(texto, 4)
                termos = texto
                termos_colecao += termos
                docs_colecao = fpg.insereTermos(arq.name, termos, lists)


docs_colecao = fpg.emLista(docs_colecao)
avg_doclen = okapibm25.mediaDoc(tam_list, qtdDocs)
cont_termos = fpg.preencheTermos(termos_colecao, lists)

idf = okapibm25.idf(qtdDocs, cont_termos)

score = okapibm25.OkapiBM25(docs_colecao, cont_termos, avg_doclen, qtdDocs, idf)

#cria um arquivo com os score do bm25
okapibm25.arquivo(score)
