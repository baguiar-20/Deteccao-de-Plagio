import glob
import re
import funcaoPreC as fpre

# processar os tokens antes para o pre processamento

tokensSymC = fpre.token("tokenSymbolsC.txt")

docs_colecao = []
termos_colecao_c = []
list_c = []
cont_c = 0

# pre processamento
for file in glob.glob("/home/brendaum/Área de Trabalho/PIBIC/Codigos/codigos_modelos/documentos/*.txt"):
    print()
    print("Name of the file:", file)
    fp = open(file, "r", -1, 'utf-8')
    codeTEXT = fp.readlines()
    #print(codeTEXT)
    print()
    cont_c += 1
    texto = fpre.removeSpace(codeTEXT)

    texto = fpre.tokensS(codeTEXT, tokensSymC)
    #print(texto)
    #print()
    texto = fpre.tokensP(codeTEXT)
    #print(texto)
    #print()
    texto = fpre.normaliza(codeTEXT)
    
    tam_doc = len(texto)

    texto = fpre.calcNgram(texto, 4)
    #print(texto)
    #print()
    termos = texto
    termos_colecao_c += termos
    docs_colecao = fpre.insertTERMOS(file, termos, list_c, tam_doc)
    print()
#print()
termos_colecao_c = fpre.removeREPEATED(termos_colecao_c)
cont_termos = fpre.preencheTERMOS(termos_colecao_c, list_c)
print(cont_termos)
#print()
#idf_colection_c = fpre.calculaIDF(cont_termos, cont_c)

#print(idf_colection_c)


