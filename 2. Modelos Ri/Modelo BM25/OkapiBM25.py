import numpy as np
import math as mt
import glob

'''fórmula  para IDF tem desvantagens para termos que aparecem em mais da metade dos documentos 
do corpus. O IDF desses termos é negativo; portanto, para quaisquer dois documentos 
quase idênticos, um que contenha o termo pode ser classificado como inferior ao que não contém'''

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


    
def idf(qtdDocs,cont_termos):
    idf ={}
    for term, num in cont_termos.items():
        # dessa 
        #t = mt.log((qtdDocs-num + 0.5) / (num+0.5), 2.71828)
        #t = mt.log(1+((qtdDocs-num + 0.5) / (num+0.5)), 2.71828)
        #t = mt.log(qtdDocs/num, 2.71828)
        t = mt.log( (qtdDocs + 0.5) / (num+0.5), 2.71828)
        
        idf[term] = t
    return idf


########################################################################################

def OkapiBM25(docs_colecao, cont_termos, avg_doclen, qtdDocs, idf,  K1 = 1, b = 0.75):
    tf = 0
    okapi = {}
    cont = 0
    bm = 0.0
    for busca in docs_colecao:
        for consulta in docs_colecao:
            for term, num in cont_termos.items():
                if (term in busca[1]) and (term in consulta[1]):
                    tf = consulta[1].count(term)
                    tam = len(consulta[1])
                    bm += idf.get(term) * ( tf *(K1+1) / (K1 * ( 1-b + b * tam/avg_doclen ) + tf) )
            okapi[cont] = [busca[0],consulta[0],bm]
            cont += 1
            bm = 0        
    return okapi
