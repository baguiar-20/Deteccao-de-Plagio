import glob, os, math, errno, re, fnmatch
import numpy as np
from os.path import isfile
from re import sub
from collections import defaultdict
"""
    Módulo com funções que realizam o pré processamento e 
    e a substituição dos tokens no código
"""


# passa como parametro um arquivo de tokens e o transforma em uma lista de tuplas
def token(arquivoToken): 
    fp = open(arquivoToken)
    tokens = fp.readlines()
    for i in range(len(tokens)):
        tokens[i] = tokens[i].replace("\n", "")
        tokens[i] = tuple(tokens[i].split(' '))
    return tokens


#arquivos em c
#troca espaços vazios por token AB e remove comentarios
def removeSpace(texto):
    for i in range(len(texto)):
        texto[i] = texto[i].replace("\n", "")
        texto[i] = texto[i].replace("\\n", "")
        texto[i] = texto[i].replace(" ", "AB")
        texto[i] = texto[i].replace("\s", "")
        texto[i] = texto[i].replace("\t", "")
    for i in range(len(texto)):
        x = texto[i]
        texto[i] = re.sub(r'//.*', '//', x) 
    return texto



def tokensS(texto, tokens): # troca os simbolos por tokens
    x = ' '
    k = ' '
    for i in range(len(texto)):
        texto[i] = texto[i].replace("::" ,"tg")
        texto[i] = texto[i].replace("&&" ,"ob")
        texto[i] = texto[i].replace("||" ,"oc")
        texto[i] = texto[i].replace("<<" ,"js")
        texto[i] = texto[i].replace("/*" ,"ir")
        texto[i] = texto[i].replace("*/" ,"is")
        texto[i] = texto[i].replace("/*" ,"ir")
        texto[i] = texto[i].replace("//" ,"jt")
        texto[i] = texto[i].replace("++" ,"it")
        texto[i] = texto[i].replace("--" ,"iu")

    for i in range(len(texto)):
        x = texto[i]
        for c in x:
            k = c
            for j in range(len(tokens)):
                if(k == tokens[j][0]):
                    k = tokens[j][1]
            if(c != k):
                x = x.replace(c,k)
        texto[i] = x
    return texto
#troca palavras reservadas da linguagem C para tokens (versao preguicosa)
def tokensP(texto):
    for i in range(len(texto)):
        texto[i] = texto[i].replace("unsigned", "hd")
        texto[i] = texto[i].replace("register" ,"gs")
        texto[i] = texto[i].replace("volatile", "hf")
        
        texto[i] = texto[i].replace("typedef", "hb")
        texto[i] = texto[i].replace("default" ,"gg")
        texto[i] = texto[i].replace("isalnum","hh")
        texto[i] = texto[i].replace("isalpha", "hi")
        texto[i] = texto[i].replace("isdigit", "hj")
        texto[i] = texto[i].replace("isspace", "hk")
        texto[i] = texto[i].replace("fprintf", "jj")
        texto[i] = texto[i].replace("sprintf", "jl")
        texto[i] = texto[i].replace("strncmp", "ij")
        texto[i] = texto[i].replace("scandir", "im")
        texto[i] = texto[i].replace("include" ,"ni")
        
        texto[i] = texto[i].replace("double", "gh")
        texto[i] = texto[i].replace("extern" ,"gl")
        texto[i] = texto[i].replace("signed", "gv")
        texto[i] = texto[i].replace("sizeof", "gx")
        texto[i] = texto[i].replace("static", "gw")
        texto[i] = texto[i].replace("struct", "gz")
        texto[i] = texto[i].replace("switch" ,"ha")
        texto[i] = texto[i].replace("fclose", "hs")
        texto[i] = texto[i].replace("getchar", "jn")
        texto[i] = texto[i].replace("printf", "jo")
        texto[i] = texto[i].replace("sscanf", "jq")
        texto[i] = texto[i].replace("getenv", "ib")
        texto[i] = texto[i].replace("malloc","id")
        texto[i] = texto[i].replace("strchr", "if")
        texto[i] = texto[i].replace("strcmp", "ig")
        texto[i] = texto[i].replace("strcpy", "ih")
        texto[i] = texto[i].replace("strlen", "ii")
        texto[i] = texto[i].replace("strstr", "ik")
        texto[i] = texto[i].replace("strtok", "il")
        texto[i] = texto[i].replace("sizeof", "in")
        texto[i] = texto[i].replace("typeof", "io")
        texto[i] = texto[i].replace("locale", "ja")
        texto[i] = texto[i].replace("stdlib", "jd")
        texto[i] = texto[i].replace("string", "je")
        texto[i] = texto[i].replace("clrscr", "og")
        texto[i] = texto[i].replace("return", "ci")
        
        
        texto[i] = texto[i].replace("const" ,"ge")
        texto[i] = texto[i].replace("union", "hc")
        texto[i] = texto[i].replace("floor", "hn")
        texto[i] = texto[i].replace("log10", "ho")
        texto[i] = texto[i].replace("fgetc", "jg")
        texto[i] = texto[i].replace("fgets", "jh")
        texto[i] = texto[i].replace("fopen", "ji")
        texto[i] = texto[i].replace("fputc", "jm")
        texto[i] = texto[i].replace("scanf", "jr")
        texto[i] = texto[i].replace("stdio", "jc")
        texto[i] = texto[i].replace("getch", "oe")
        texto[i] = texto[i].replace("conio", "of")
        
        texto[i] = texto[i].replace("auto" ,"ga")
        texto[i] = texto[i].replace("case" ,"gc")
        texto[i] = texto[i].replace("char" ,"gd")
        texto[i] = texto[i].replace("enum", "gk")
        texto[i] = texto[i].replace("goto", "go")
        texto[i] = texto[i].replace("long", "gr")
        texto[i] = texto[i].replace("void", "he")
        texto[i] = texto[i].replace("ceil", "hl")
        texto[i] = texto[i].replace("sqrt", "hr")
        texto[i] = texto[i].replace("feof", "ht")
        texto[i] = texto[i].replace("getc", "hu")
        texto[i] = texto[i].replace("gets", "hv")
        texto[i] = texto[i].replace("puts", "jp")
        texto[i] = texto[i].replace("atof", "hx")
        texto[i] = texto[i].replace("atoi", "hw")
        texto[i] = texto[i].replace("atol", "hz")
        texto[i] = texto[i].replace("free", "ic")
        texto[i] = texto[i].replace("rand", "ie")
        texto[i] = texto[i].replace("time", "jf")
        texto[i] = texto[i].replace("main", "od")

        texto[i] = texto[i].replace("exp", "hm")
        texto[i] = texto[i].replace("log", "hp")
        texto[i] = texto[i].replace("pow", "hq")
        texto[i] = texto[i].replace("int" ,"dw")
        texto[i] = texto[i].replace("for" ,"bv")

        texto[i] = texto[i].replace("do" ,"gi")   
        
    return texto

def normaliza(texto):
    texto = ''.join(texto)
    texto = texto.lower()
    return texto



def calcNgram(listapalavras, n):#calcula as n-gramas dos tokens gerados
    ngrams = []
    vocabulario = []
    for i in range(len(listapalavras)-(n-1)):
        ngrams.append(listapalavras[i:i+n])
    for n, i in enumerate(ngrams):
        auxi = "".join(str(x) for x in i)
        vocabulario.append(auxi)
    return vocabulario

def insertTERMOS(file, vocab_atual, colecao, tam_doc):
    key_file = file
    vocab_file = vocab_atual
    tam_file = tam_doc
    colecao.append({key_file: vocab_file, "tam": tam_file})
    return colecao

def preencheTERMOS(termos_colecao_c, list_c): #Nº de doc em q o termo ocorre na coleção
    termos_number = np.array(len(termos_colecao_c))
    for i in termos_number:
        cont = 0
        for j in list_c:
            for x in j.items():
                if i in x[1]:
                    cont +=1
                    termos_number[i] = cont
    return termos_number

def removeREPEATED(vocaburepetido): #remove elementos repetidos de listas
    final_vocabu = [] 
    for num in vocaburepetido: 
        if num not in final_vocabu: 
            final_vocabu.append(num) 
    return final_vocabu



            


