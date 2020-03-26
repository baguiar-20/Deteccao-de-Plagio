import glob
import re
import funcaoPreC as fpre
import BM25 as bm25

# processar os tokens antes para o pre processamento

tokensSymC = fpre.token("tokenSymbolsC.txt")
docs_colecao = []
termos_colecao_c = []
list_c = []
cont_c = 0
tam_list_c = []
tam_doc= {}
tam_list = {}
cont = 0
i = 0
score = []
md = 0

# pre processamento

for file in glob.glob("/home/brendaum/Área de Trabalho/PIBIC/Codigos/codigos_modelos/Docs_Linguagem_C/*.txt"):
    print()
    print("Name of the file:", file)
    fp = open(file, "r", -1, 'utf-8')
    #contDocs += i 
    codeTEXT = fp.readlines()
    #print(codeTEXT)
    print()
    texto = fpre.removeSpace(codeTEXT)
    texto = fpre.tokensS(codeTEXT, tokensSymC)
    texto = fpre.tokensP(codeTEXT)
    texto = fpre.normaliza(codeTEXT)
    tam_doc = len(texto)
    tam_list[i] = len(texto)
    i += 1
    texto = fpre.calcNgram(texto, 4)
    termos = texto
    termos_colecao_c += termos
    docs_colecao, tam_colecao = fpre.insertTERMOS(file, termos, list_c, tam_list_c, tam_doc)
    print()

avg_doclen = bm25.mediaDoc(tam_list, i)
cont_termos = fpre.preencheTERMOS(termos_colecao_c, list_c)
termosConsulta = bm25.termosConsulta(docs_colecao) 
#retorna o documento de busca, documento de consulta, o termo semelhante e a quantidade de vezes que ele se repete

#print()

#print("Numero total de documentos: ", i)
#print()
#print("Tamanho de cada documento: ")

#print()
#print("Media dos documentos(avg_doclen): ", avg_doclen)
#print()
#print("Nº de documentos em q o termo ocorre na coleção", cont_termos)
#print()

#print("Numero de termo da consulta ocorre no documento: ")
#print(termosConsulta)


#score = bm25.OkapiBM25(docs_colecao)

#print(score)

#print(termosConsulta)

score = bm25.OkapiBM25(docs_colecao, cont_termos, i,avg_doclen,  termosConsulta,tam_colecao)

for i in score:
    print(score[i])



#for i in termosConsulta:
    #print(termosConsulta[i][2])